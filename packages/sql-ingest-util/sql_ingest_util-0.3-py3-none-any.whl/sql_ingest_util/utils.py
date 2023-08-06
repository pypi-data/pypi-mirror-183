import ruamel.yaml


def get_configs_dict_from_yaml(yaml_path):
    configs_dict = ruamel.yaml.round_trip_load(open(yaml_path, "rb"), preserve_quotes=True)
    return configs_dict


def get_yaml_from_configs_dict(configs_dict, yaml_output_path):
    ruamel.yaml.round_trip_dump(configs_dict, open(yaml_output_path, "w"), default_flow_style=False)
