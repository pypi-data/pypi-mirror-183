import io
from typing import ClassVar, Dict, Any, List, Set

import boto3
import pandas as pd
from botocore.exceptions import ClientError
from tinydb import Storage, TinyDB
from tinydb.storages import MemoryStorage

from rplus_constants.rplus_utils_module import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME


class S3WrapperStorage(Storage):
    def __init__(self, bucket: str, file: str, table_name: str):
        self.bucket = bucket
        self.file = file
        self.table_name = table_name.lower()
        self.client = boto3.resource(
            "s3",
            region_name=REGION_NAME,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )

    def construct_load_csv(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Convert from pandas format to tinydb format
        :param records: list of dictionary data
        :return:
        """
        tmp = {self.table_name: {}}
        for idx, value in enumerate(records):
            rec_id = value.pop("internal_id", idx)
            table_name = value.pop("internal_table", self.table_name)
            tmp[table_name][rec_id] = value
        return tmp

    def read_from_s3_csv(self) -> pd.DataFrame:
        """Read data from bucket and convert as dataframe
        :return: pandas dataframe
        """
        try:
            obj = self.client.Object(self.bucket, self.file)
            resp = obj.get()
            data = io.BytesIO(resp["Body"].read())
            if "csv" in self.file:
                return pd.read_csv(data, compression="gzip")

            return pd.read_pickle(data, compression="gzip")
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return pd.DataFrame()

            return pd.DataFrame()

    def read(self) -> Dict[str, Any]:
        """Read data from s3 to buffer
        :return: dictionary data
        """
        df = self.read_from_s3_csv()
        if len(df) == 0:
            return {}

        resp = df.to_dict(orient="records")
        tinydb_formatted = self.construct_load_csv(resp)
        return tinydb_formatted

    def construct_write_csv(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Convert from tinydb format to pandas csv format
        :param data: dictionary data
        :return:
        """
        tmp = []
        for key, value in data[self.table_name].items():
            tmp.append({"internal_table": self.table_name, "internal_id": key, **value})

        return tmp

    def create_writer(self, data: Dict[str, Any]) -> io.BytesIO:
        """Create writer buffer from pandas to bytes
        :param data: dictionary data
        :return:
        """
        csv_format = self.construct_write_csv(data)
        df = pd.DataFrame(csv_format)
        writer = io.BytesIO()

        if "csv" in self.file:
            df.to_csv(writer, index=False, compression="gzip")
        if "pkl" in self.file:
            df.to_pickle(writer, compression="gzip")

        writer.seek(0)
        return writer

    def write(self, data: Dict[str, Any]) -> bool:
        """Write data to s3 storage file
        :param data: dictionary data
        :return: boolean status
        """
        if len(data[self.table_name]) == 0:
            return True

        writer = self.create_writer(data)
        self.client.Object(self.bucket, self.file).put(Body=writer.getvalue())
        return True

    def close(self):
        pass


class S3Database:
    def __init__(self, db: TinyDB):
        self.db = db

    @classmethod
    def init_db_from_s3(cls, file_path: str, table_name: str) -> "S3Database":
        """Init tiny db from s3 storage
        :param file_path: string file path name
        :param table_name: string table name
        :return: current object class
        """
        db = TinyDB(
            bucket=BUCKET_NAME,
            file=file_path,
            storage=S3WrapperStorage,
            table_name=table_name.lower(),
        )
        return cls(db)

    @classmethod
    def init_from_memory(cls) -> ClassVar:
        """Initialize new database from memory only
        :return: current class object
        """
        return cls(TinyDB(storage=MemoryStorage))

    def table(self, table_name: str) -> TinyDB:
        """Select for specified database name
        :param table_name: string database name
        :return: object tony db
        """
        self.db.table(table_name.lower())
        return self.db

    def tables(self) -> Set[str]:
        """Select for specified database name
        :return: object tony db
        """
        return self.db.tables()

    def insert_multi(self, table_name: str, datas: List[Dict[str, Any]]) -> bool:
        """Inserting multiple data in one go
        :param table_name: string of table name
        :param datas: list of dictionary data
        :return: boolean true or false
        """
        self.db.table(table_name.lower()).insert_multiple(datas)
        return True
