from io import StringIO

import boto3
from constants.rplus_utils_module.constant import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    REGION_NAME,
)
from pandas import read_csv, DataFrame

from utils_module.logger import Logging


class S3Service:
    def __init__(self, boto_object: boto3.resource):
        self.resource = boto_object

    @classmethod
    def from_connection(
        cls,
        access_key: str = AWS_ACCESS_KEY,
        secret_key: str = AWS_SECRET_KEY,
        region_name: str = REGION_NAME,
    ) -> "S3Service":
        try:
            conn = boto3.resource(
                "s3",
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region_name,
            )

        except Exception as e:
            raise "boto3 resource object creation failed {}".format(str(e))

        return cls(conn)

    def read_csv_from_s3(
        self,
        bucket_name=None,
        object_name=None,
    ) -> DataFrame:
        """
        This function returns dataframe object of csv file stored in S3
        :param bucket_name: Name of the bucket where csv is stored
        :param object_name: Path of the object in S3
        :return: dataframe object pandas
        """
        content_object = self.resource.Object(bucket_name, object_name)
        try:
            csv_string = content_object.get()["Body"].read().decode("utf-8")
            df = read_csv(StringIO(csv_string))
            Logging.info("File {} has been read successfully".format(object_name))
            return df

        except Exception as e:
            raise "Unable to find file no such file exists {}".format(str(e))

    def write_csv_to_s3(
        self,
        bucket_name=None,
        object_name=None,
        df_to_upload=None,
    ) -> None:
        """
        Function to write csv in S3
        :param bucket_name: Name of the bucket where csv shall be stored
        :param object_name: Path of the object in S3
        :param df_to_upload: dataframe to be stored as csv
        :return:
        """
        try:
            csv_buffer = StringIO()
            df_to_upload.to_csv(csv_buffer, header=True, index=False)
            content_object = self.resource.Object(bucket_name, object_name)
            content_object.put(Body=csv_buffer.getvalue())
            Logging.info("Successfully dump data into s3")
        except Exception as e:
            raise ("Error while dumping into s3 for the object {}".format(str(e)))
