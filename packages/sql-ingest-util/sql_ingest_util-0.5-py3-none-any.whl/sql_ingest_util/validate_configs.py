import re
import string
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

from utils.yaml_config_convertor import YamlConfigConvertor


@dataclass
class ValidateMandatoryConfigs:
    pm: str
    user: str
    start_date: str
    schedule_interval: str
    cluster_name: str
    table_name: str
    partition_columns: List[str]
    custom_time: Dict[str, int]

    def __init__(self, pm, user, start_date, schedule_interval, cluster_name, table_name, partition_columns,
                 custom_time):
        self.pm = pm
        self.user = user
        self.start_date = start_date
        self.schedule_interval = schedule_interval
        self.cluster_name = cluster_name
        self.table_name = table_name
        self.partition_columns = partition_columns
        self.custom_time = custom_time

    def validate_person_name(self):
        if not set(self.pm) <= set(string.ascii_lowercase + '_'):
            raise Exception("Invalid PM name, Only lowercase alphabets and '_' are allowed")
        if not set(self.user) <= set(string.ascii_lowercase + '_'):
            raise Exception("Invalid User name, Only lowercase alphabets and '_' are allowed")

    def validate_start_date(self):
        if self.start_date != datetime.strptime(self.start_date, "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%dT%H:%M:%S'):
            raise ValueError("Valid start date format is yyyy-mm-ddThh:mm:ss")

    def validate_schedule_interval(self):
        allowed_schedule_intervals = ["HOURLY", "DAILY", "WEEKLY", "MONTHLY"]
        if self.schedule_interval not in allowed_schedule_intervals:
            raise ValueError("Valid schedule intervals are HOURLY, DAILY, WEEKLY, MONTHLY")

    def validate_cluster_name(self):
        if not len(self.cluster_name) <= 20:
            raise Exception("Cluster name should NOT exceed 20 chars !!!")
        if not set(self.cluster_name) <= set(string.ascii_lowercase + string.digits + '-'):
            raise Exception("Invalid Cluster name, Only lowercase alphabets, digits and '-' are allowed")

    def validate_table_name(self):
        if not set(self.table_name) <= set(string.ascii_lowercase + string.digits + '_'):
            raise Exception("Invalid Table name, Only lowercase alphabets, digits and '_' are allowed")

    def validate_partition_columns(self):
        if not len(self.partition_columns) > 0:
            raise Exception("Partition Columns can not be empty !!!")

    def validate_custom_time(self):
        if not 0 <= self.custom_time['minute'] <= 59:
            raise ValueError("'minute' value expected between 0 and 59")
        if not 0 <= self.custom_time['hour'] <= 59:
            raise ValueError("'hour' value expected between 0 and 59")
        if not 0 <= self.custom_time['weekday'] <= 6:
            raise ValueError("'weekday' value expected between 0 and 6")
        if not 1 <= self.custom_time['monthday'] <= 31:
            raise ValueError("'monthday' value expected between 1 and 31")

    def validate_mandatory_configs(self):
        self.validate_person_name()
        self.validate_start_date()
        self.validate_schedule_interval()
        self.validate_cluster_name()
        self.validate_table_name()
        self.validate_partition_columns()
        self.validate_custom_time()

    def validate_dag_name(self, dag_name):
        if not dag_name.lower() == self.table_name:
            raise ValueError(f"Expected dag_name {self.table_name.upper()} but got {dag_name}")

    def validate_view_name(self, view_name):
        if not view_name == self.table_name:
            raise ValueError(f"Expected dag_name {self.table_name} but got {view_name}")


def validate_backfill(backfill):
    if not type(backfill) == bool:
        raise TypeError(f"Expected backfill of type {bool} but got {type(backfill)}")


def validate_bucket_path(file_store_bucket_path, table_bucket_path):
    bucket_path = "gs://production-data-reports"
    if not file_store_bucket_path == bucket_path:
        raise ValueError(f"'bucket_path' expects '{bucket_path}' but got '{file_store_bucket_path}'")
    if not table_bucket_path == bucket_path:
        raise ValueError(f"'bucket_path' expects '{bucket_path}' but got '{table_bucket_path}'")


def validate_base_path(file_store_base_path, table_base_path):
    if not file_store_base_path == table_base_path:
        raise ValueError(f"'base_path' {file_store_base_path} is different from '{table_base_path}' Unexpected!!")


def validate_sql_query_against_args(sql_flow_config):
    query = sql_flow_config['sql']
    if "select*" in query.lower().replace("\n", "").replace(" ", ""):
        raise Exception("'SELECT *' is unexpected in query !!!")

    args = []
    if 'args' in sql_flow_config:
        args = sql_flow_config['args']

    args_from_query = re.findall('({{\w+}})', query)
    if len(args) < len(args_from_query):
        raise Exception(
            f"Got {len(args_from_query)} args from query but only {len(args)} args are defined !!!")

    for index in range(len(args_from_query)):
        args_from_query[index] = args_from_query[index][2:-2]
    args_from_query = list(set(args_from_query))

    args_var_name = []
    for arg in args:
        args_var_name.append(arg['var_name'])

    for arg in args_from_query:
        if arg not in args_var_name:
            raise Exception(f"{arg} argument has been used in query, but not defined !!!")


def validate_final_yaml_file(input_file_path):
    config_convertor = YamlConfigConvertor(input_yaml_path=input_file_path)
    configs_dict = config_convertor.get_configs_dict_from_yaml()

    domain = configs_dict['domain']
    dag_configs = configs_dict['dag_configs'][0]
    run_configs = dag_configs['run_config']
    job_configs = dag_configs['job_configs'][0]
    flow_config = job_configs['flow_config']

    pm = configs_dict['pm']
    user = configs_dict['user']
    dag_name = dag_configs['name']
    backfill = dag_configs['backfill']

    cluster_name = run_configs['cluster_config']['name']
    start_date = run_configs['schedule_config']['start_date']
    schedule_interval = run_configs['schedule_config']['schedule_interval']
    custom_time = run_configs['schedule_config']['custom_time']

    bucket_path = job_configs['write_store']['bucket_path']
    base_path = job_configs['write_store']['base_path']
    partition_columns = job_configs['write_store']['partition_columns']

    table_name = job_configs['table_view_config']['table_name']
    table_bucket_path = job_configs['table_view_config']['bucket_path']
    table_base_path = job_configs['table_view_config']['base_path']
    view_name = job_configs['table_view_config']['view_name']

    cluster_name_prefix = domain.lower().replace("_", "-")
    cluster_name = cluster_name[len(cluster_name_prefix)+1:]

    validate = ValidateMandatoryConfigs(pm=pm,
                                        user=user,
                                        start_date=start_date,
                                        schedule_interval=schedule_interval,
                                        cluster_name=cluster_name,
                                        table_name=table_name,
                                        partition_columns=partition_columns,
                                        custom_time=custom_time)

    validate.validate_mandatory_configs()
    validate.validate_dag_name(dag_name=dag_name)
    validate.validate_view_name(view_name=view_name)

    validate_backfill(backfill=backfill)
    validate_bucket_path(file_store_bucket_path=bucket_path, table_bucket_path=table_bucket_path)
    validate_base_path(file_store_base_path=base_path, table_base_path=table_base_path)
    validate_sql_query_against_args(sql_flow_config=flow_config)

    print("\n Validation SUCCESSFUL !!")
