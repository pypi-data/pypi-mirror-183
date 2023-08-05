from abc import ABCMeta, abstractmethod
import json
import time
from intelliw.datasets.datasource_base import AbstractDataSourceWriter, DataSourceWriterException, DataSourceType as DST
from intelliw.utils import iuap_request
from intelliw.utils.logger import _get_framework_logger
from intelliw.utils.util import get_json_encoder
from intelliw.config import config
import pandas as pd

logger = _get_framework_logger()


class AbstractEngineWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, data, **kwargs):
        pass


class UserWriter(AbstractEngineWriter):
    def write(self, data, **kwargs):
        pass


class SqlWriter(AbstractEngineWriter):
    def __init__(self) -> None:
        self.uri = ""
        self.table_name = ""
        self.batch_size = 10000
        self.engine = self.__get_engine()

    def __get_engine(self):
        from intelliw.utils.database import connection
        connection.get_engine(self.driver, uri=self.uri)

    def write(self, data, **kwargs):
        frame = pd.DataFrame(data["result"], columns=data["mate"])
        start_index = 0
        end_index = self.batch_size if self.batch_size < len(
            frame) else len(frame)

        frame = frame.where(pd.notnull(frame), None)
        if_exists_param = 'replace'

        while start_index != end_index:
            logger.info("Writing rows %s through %s" %
                        (start_index, end_index))
            frame.iloc[start_index:end_index, :].to_sql(
                con=self.engine, name=self.table_name, if_exists=if_exists_param)
            if_exists_param = 'append'

            start_index = min(start_index + self.batch_size, len(frame))
            end_index = min(end_index + self.batch_size, len(frame))


class IntellivWriter(AbstractEngineWriter):
    def __init__(self, source_addr, dataSourceId, inferId, tenantId):
        self.source_addr = source_addr
        self.dataSourceId = dataSourceId
        self.inferId = inferId
        self.tenantId = tenantId

    def write(self, data, start_time):
        end_time = int(time.time() * 1000)
        result = {
            "dataSourceId": self.dataSourceId,
            "serviceId": self.inferId,
            "startTime": start_time,
            "endTime": end_time,
            "tenantId": self.tenantId,
            'data': json.dumps(data, cls=get_json_encoder())
        }

        res = iuap_request.post_json(url=self.source_addr, json=result)
        res.raise_for_status()
        res_data = res.json
        return res_data


class DataSourceWriter(AbstractDataSourceWriter):
    def __init__(self, **kwargs):
        self.writer_info = kwargs
        self.writer_type = kwargs.get("writer_type")
        self.inferId = config.INFER_ID,
        self.tenantId = config.TENANT_ID
        try:
            self.writer = self.__get_writer()
        except Exception as e:
            raise DataSourceWriterException(f"Data Output Initialization Error: {e}")

    def __get_writer(self) -> AbstractEngineWriter:
        if self.writer_type == DST.SQL:
            return SqlWriter()
        elif self.writer_type in (DST.IW_FACTORY_DATA, DST.INTELLIV):
            source_addr = self.writer_info["source_addr"]
            source_id = self.writer_info["source_id"]
            return IntellivWriter(source_addr, source_id, self.inferId, self.tenantId)
        else:
            return UserWriter()

    def write(self, data, **kwargs):
        try:
            self.writer.write(data=data, **kwargs)
        except Exception as e:
            raise DataSourceWriterException(f"Data Output Process error: {e}")
