import boto3
import pandas as pd
import copy
import io


class Config:
    def __init__(self, access_key_id: str = None, secret_access_key: str = None):
        try:
            if access_key_id is None or secret_access_key is None:
                self.__s3_client = boto3.client('s3')
            else:
                self.__s3_client = boto3.client(
                    's3',
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key
                )
        except Exception as e:
            raise e

    @staticmethod
    def __compression_type(key, compression):
        try:
            extension = key.split('.')[-1]
            compression_dict = {'gz': 'gzip', 'bz2': 'bz2', 'zip': 'zip', 'xz': 'xzy'}
            return compression_dict[extension] if extension in compression_dict.keys() else compression
        except Exception as e:
            raise e

    @staticmethod
    def __count_df_rows(df):
        try:
            return df.count()[0]
        except Exception as e:
            return 0

    @staticmethod
    def __ignore_key(key):
        key_upper_case = key.upper()
        return key_upper_case.startswith('_SUCCESS') or key_upper_case.startswith('_STARTED_') or key_upper_case. \
            startswith('_COMMITTED_')

    @staticmethod
    def __segregate_path(s3_path):
        try:
            s3_path = s3_path[5:].split('/')
            bucket, prefix = s3_path[0], '/'.join(s3_path[1:])
            return bucket, prefix
        except Exception as e:
            raise e

    def __read_s3_data_in_df(self, file_type, bucket, key, header, compression, skip_rows: int = 0,
                             skip_footer: int = 0, sep: str = ','):
        try:
            resources = self.__s3_client.get_object(Bucket=bucket, Key=key)
            file_content = io.BytesIO(resources['Body'].read())
            compression_type = self.__compression_type(key, compression)

            header = 0 if header is True else None
            if file_type == 'csv':
                df = pd.read_csv(file_content, header=header, compression=compression_type, skiprows=skip_rows,
                                 skipfooter=skip_footer, sep=sep)
            elif file_type == 'parquet':
                df = pd.read_parquet(file_content)
            elif file_type == 'excel':
                df = pd.read_excel(file_content, header=header, skiprows=skip_rows,
                                   skipfooter=skip_footer)
            return df
        except Exception as e:
            raise e

    def check_s3_path(self, s3_path: str):
        try:
            bucket, prefix = self.__segregate_path(s3_path)
            objects = self.__s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            if len(objects['Contents']) != 0:
                return True
        except KeyError:
            return False
        except Exception as e:
            raise e

    def check_duplicate_data(self, s3_path: str, file_type: str, header: bool = True, compression: str = 'infer',
                             skip_rows: int = 0, skip_footer: int = 0, sep: str = ','):
        try:
            if file_type not in ['parquet', 'csv', 'excel']:
                raise ValueError(f"File type should be one from ['parquet', 'csv', 'excel']")

            bucket, prefix = self.__segregate_path(s3_path)
            objects = self.__s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            output_list = []
            for obj in objects['Contents']:
                key = obj["Key"]
                final_key = key.split('/')[-1]
                if not key.endswith("/") and not self.__ignore_key(final_key):
                    df = self.__read_s3_data_in_df(file_type, bucket, key, header, compression, skip_rows, skip_footer,
                                                   sep)
                    duplicate_count = len(df) - len(df.drop_duplicates())
                    if duplicate_count != 0:
                        output_list.append({'report_name': final_key, 'error': True,
                                            'message': f'Number of duplicate row is {duplicate_count}'})
                    else:
                        output_list.append({'report_name': final_key, 'error': False,
                                            'message': 'No duplicate row found'})
            return output_list
        except Exception as e:
            raise e

    def check_empty_data(self, s3_path: str, file_type: str, header: bool = True, compression: str = 'infer',
                         skip_rows: int = 0, skip_footer: int = 0, sep: str = ','):
        try:
            if file_type not in ['parquet', 'csv', 'excel']:
                raise ValueError(f"File type should be one from ['parquet', 'csv', 'excel']")

            bucket, prefix = self.__segregate_path(s3_path)
            objects = self.__s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            output_list = []

            for obj in objects['Contents']:
                key = obj["Key"]
                final_key = key.split('/')[-1]
                if not key.endswith("/") and not self.__ignore_key(final_key):
                    df = self.__read_s3_data_in_df(file_type, bucket, key, header, compression, skip_rows, skip_footer,
                                                   sep)
                    if self.__count_df_rows(df) != 0:
                        output_list.append({'report_name': final_key, 'error': False,
                                            'message': 'Report has data'})
                    else:
                        output_list.append(
                            {'report_name': final_key, 'error': True, 'message': 'Report is empty'})
            return output_list
        except Exception as e:
            raise e

    def check_schema(self, s3_path: str, file_type: str, expected_schema: list, header: bool = True,
                     compression: str = 'infer', skip_rows: int = 0, skip_footer: int = 0, sep: str = ','):
        try:
            if file_type not in ['parquet', 'csv', 'excel']:
                raise ValueError(f"File type should be one from ['parquet', 'csv', 'excel']")
            bucket, prefix = self.__segregate_path(s3_path)
            objects = self.__s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            output_list = []

            for obj in objects['Contents']:
                key = obj["Key"]
                final_key = key.split('/')[-1]
                if not key.endswith("/") and not self.__ignore_key(final_key):
                    df = self.__read_s3_data_in_df(file_type, bucket, key, header, compression, skip_rows, skip_footer,
                                                   sep)
                    current_header_column = [str(i) for i in list(df.columns)]
                    header_column = [str(i) for i in list(df.columns)]
                    sorted_header = copy.copy(header_column)
                    sorted_header.sort()
                    sorted_expected_schema = copy.copy(expected_schema)
                    sorted_expected_schema.sort()

                    # If file_type == parquet, ignore the schema order
                    if file_type == 'parquet':
                        header_column.sort()
                        expected_schema.sort()

                    if header_column == expected_schema:
                        output_list.append({'report_name': final_key, 'error': False, 'message': 'Success',
                                            'report_schema': current_header_column})
                    elif sorted_header == sorted_expected_schema:
                        output_list.append({'report_name': final_key, 'error': True,
                                            'message': 'Report schema order is different than expected',
                                            'report_schema': current_header_column})
                    else:
                        output_list.append({'report_name': final_key, 'error': True,
                                            'message': 'Report schema is different than expected',
                                            'report_schema': current_header_column})
            return output_list
        except Exception as e:
            raise e
