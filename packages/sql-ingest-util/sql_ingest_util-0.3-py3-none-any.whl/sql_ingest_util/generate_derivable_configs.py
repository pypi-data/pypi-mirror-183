
class DerivableConfigs:
    table_name: str

    def __init__(self, table_name):
        self.table_name = table_name

    def get_dag_name(self):
        return self.table_name.upper()

    def get_cluster_name(self):
        cluster_name_prefix = "rapido-sql-ingest"
        cluster_name = self.table_name.replace("_", "-")
        return f"{cluster_name_prefix}-{cluster_name}"

    def get_base_path(self, base_path):
        return base_path + self.table_name

    def get_view_name(self):
        return self.table_name


def get_derived_configs(table_name, base_path):
    config = DerivableConfigs(table_name)
    return {
        "dag_name": config.get_dag_name(),
        "cluster_name": config.get_cluster_name(),
        "base_path": config.get_base_path(base_path),
        "view_name": config.get_view_name()
    }
