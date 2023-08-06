import os
from dataclasses import dataclass, field
from typing import Dict, List

from sql_ingest_util.validate_configs import ValidateMandatoryConfigs
from sql_ingest_util.utils.yaml_config_convertor import YamlConfigConvertor


@dataclass
class SqlIngestConfigs:
    pm: str
    user: str
    start_date: str
    schedule_interval: str
    cluster_name: str
    table_name: str
    partition_columns: List[str]

    dag_name: str
    base_path: str
    view_name: str
    custom_time: Dict[str, int]
    backfill: bool = False

    def __init__(self, pm, user, start_date, schedule_interval, cluster_name, table_name, partition_columns,
                 backfill=False, custom_time=None):
        self.pm = pm.lower().replace("-", "_")
        self.user = user.lower().replace("-", "_")
        self.start_date = start_date
        self.schedule_interval = schedule_interval.upper()
        self.cluster_name = cluster_name.lower().replace("_", "-")
        self.table_name = table_name.lower().replace("-", "_")
        self.partition_columns = partition_columns
        self.backfill = backfill
        self.custom_time = {
            "minute": 0,
            "hour": 0,
            "weekday": 0,
            "monthday": 1
        }
        if custom_time is not None:
            for time_unit in custom_time:
                self.custom_time[time_unit] = custom_time[time_unit]

        self.validate_configs()

    def validate_configs(self):
        validate = ValidateMandatoryConfigs(pm=self.pm,
                                            user=self.user,
                                            start_date=self.start_date,
                                            schedule_interval=self.schedule_interval,
                                            cluster_name=self.cluster_name,
                                            table_name=self.table_name,
                                            partition_columns=self.partition_columns,
                                            custom_time=self.custom_time)
        validate.validate_mandatory_configs()

    def get_dag_name(self):
        return self.table_name.upper()

    def get_cluster_name(self, domain):
        cluster_domain = domain.lower().replace("_", "-")
        return f"{cluster_domain}-{self.cluster_name}"

    def get_base_path(self, base_path_prefix):
        return base_path_prefix + self.table_name

    def get_view_name(self):
        return self.table_name

    def assign_values_to_configs(self, configs_dict):
        domain = configs_dict['domain']
        dag_configs = configs_dict['dag_configs'][0]
        job_configs = dag_configs['job_configs'][0]
        base_path = job_configs['write_store']['base_path']

        self.dag_name = self.get_dag_name()
        self.cluster_name = self.get_cluster_name(domain)
        self.base_path = self.get_base_path(base_path_prefix=base_path)
        self.view_name = self.get_view_name()

        configs_dict['pm'] = self.pm
        configs_dict['user'] = self.user

        dag_configs['name'] = self.dag_name
        dag_configs['backfill'] = self.backfill

        dag_configs['run_config']['cluster_config']['name'] = self.cluster_name
        dag_configs['run_config']['schedule_config']['start_date'] = self.start_date
        dag_configs['run_config']['schedule_config']['schedule_interval'] = self.schedule_interval
        dag_configs['run_config']['schedule_config']['custom_time'] = self.custom_time

        job_configs['write_store']['base_path'] = self.base_path
        job_configs['write_store']['partition_columns'] = self.partition_columns

        job_configs['table_view_config']['table_name'] = self.table_name
        job_configs['table_view_config']['view_name'] = self.view_name
        job_configs['table_view_config']['base_path'] = self.base_path

        return configs_dict

    def get_yaml_file(self, output_yaml_path):
        template_yaml_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               "resources/template_sql_ingest_config.yaml")
        config_convertor = YamlConfigConvertor(input_yaml_path=template_yaml_file_path)
        template_configs_dict = config_convertor.get_configs_dict_from_yaml()
        final_configs_dict = self.assign_values_to_configs(template_configs_dict)

        config_convertor = YamlConfigConvertor(configs_dict=final_configs_dict, output_yaml_path=output_yaml_path)
        config_convertor.get_yaml_from_configs_dict()
        print(f"\n YAML file has been saved at {output_yaml_path}")
