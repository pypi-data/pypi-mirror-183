import string
from typing import List


class ValidateArgs:
    pm_name: str
    user_name: str
    dag_name: str
    cluster_name: str
    table_name: str
    partition_columns: List[str]

    def __init__(self, args_dict):
        self.pm_name = args_dict['pm_name']
        self.user_name = args_dict['user_name']
        self.dag_name = args_dict['dag_name']
        self.cluster_name = args_dict['cluster_name']
        self.table_name = args_dict['table_name']
        self.partition_columns = args_dict['partition_columns']

    def validate_cluster_name_len(self):
        if not len(self.cluster_name) <= 50:
            raise Exception("Cluster name should NOT exceed 50 chars !!!")

    def validate_table_name_len(self):
        if not len(self.table_name) <= 25:
            raise Exception("Cluster name should NOT exceed 25 chars !!!")

    def validate_partition_columns_len(self):
        if not len(self.partition_columns) > 0:
            raise Exception("Partition Columns can not be empty !!!")

    def validate_person_name_chars(self):
        if not set(self.pm_name) <= set(string.ascii_lowercase + '_'):
            raise Exception("Invalid PM name, Only lowercase alphabets and '_' are allowed")
        if not set(self.user_name) <= set(string.ascii_lowercase + '_'):
            raise Exception("Invalid User name, Only lowercase alphabets and '_' are allowed")

    def validate_dag_name_chars(self):
        if not set(self.dag_name) <= set(string.ascii_uppercase + string.digits + '_'):
            raise Exception("Invalid DAG name, Only uppercase alphabets, digits and '_' are allowed")
        
    def validate_cluster_name_chars(self):
        if not set(self.cluster_name) <= set(string.ascii_lowercase + string.digits + '-'):
            raise Exception("Invalid Cluster name, Only lowercase alphabets, digits and '-' are allowed")
            
    def validate_table_name_chars(self):
        if not set(self.table_name) <= set(string.ascii_lowercase + string.digits + '_'):
            raise Exception("Invalid Cluster name, Only lowercase alphabets, digits and '-' are allowed")


def validate_args(args_dict):
    args = ValidateArgs(args_dict=args_dict)

    args.validate_cluster_name_len()
    args.validate_table_name_len()
    args.validate_partition_columns_len()
    args.validate_person_name_chars()
    args.validate_dag_name_chars()
    args.validate_cluster_name_chars()
    args.validate_table_name_chars()
