from sql_ingest_util.validate_arguments import validate_args
from sql_ingest_util.generate_derivable_configs import get_derived_configs


def assign_values_to_configs(configs_dict, pm_name, user_name, start_date, schedule_interval,
                             table_name, partition_columns, backfill):
    dag_configs = configs_dict['dag_configs'][0]
    job_configs = dag_configs['job_configs'][0]
    base_path = job_configs['write_store']['base_path']

    derived_configs = get_derived_configs(table_name=table_name, base_path=base_path)
    dag_name = derived_configs['dag_name']
    cluster_name = derived_configs['cluster_name']
    base_path = derived_configs['base_path']
    view_name = derived_configs['view_name']

    args_dict = {
        "pm_name": pm_name,
        "user_name": user_name,
        "dag_name": dag_name,
        "cluster_name": cluster_name,
        "table_name": table_name,
        "partition_columns": partition_columns
    }
    validate_args(args_dict)

    configs_dict['pm'] = pm_name
    configs_dict['user'] = user_name

    dag_configs['name'] = dag_name
    dag_configs['backfill'] = backfill

    dag_configs['run_config']['cluster_config']['name'] = cluster_name
    dag_configs['run_config']['schedule_config']['start_date'] = start_date
    dag_configs['run_config']['schedule_config']['schedule_interval'] = schedule_interval

    job_configs['write_store']['base_path'] = base_path
    job_configs['write_store']['partition_columns'] = partition_columns

    job_configs['table_view_config']['table_name'] = table_name
    job_configs['table_view_config']['view_name'] = view_name
    job_configs['table_view_config']['base_path'] = base_path

    return configs_dict
