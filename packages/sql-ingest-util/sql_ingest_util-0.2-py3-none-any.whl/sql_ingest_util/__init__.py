from sql_ingest_util.utils import get_configs_dict_from_yaml, get_yaml_from_configs_dict
from sql_ingest_util.assign_config_values import assign_values_to_configs


def get_sql_ingest_configs(base_yaml_path, pm_name, user_name, start_date, schedule_interval,
                           table_name, partition_columns, backfill=False):

    configs_dict = get_configs_dict_from_yaml(yaml_path=base_yaml_path)
    return assign_values_to_configs(configs_dict=configs_dict,
                                    pm_name=pm_name,
                                    user_name=user_name,
                                    start_date=start_date,
                                    schedule_interval=schedule_interval,
                                    table_name=table_name,
                                    partition_columns=partition_columns,
                                    backfill=backfill)


def get_yaml_file(configs_dict, path):
    get_yaml_from_configs_dict(configs_dict=configs_dict,
                               yaml_output_path=path)
