import ruamel.yaml
from dataclasses import dataclass, field


@dataclass
class YamlConfigConvertor:
    input_yaml_path: str = None
    output_yaml_path: str = None
    configs_dict: dict = field(default_factory=dict)

    def get_configs_dict_from_yaml(self):
        self.configs_dict = ruamel.yaml.round_trip_load(open(self.input_yaml_path, "rb"), preserve_quotes=True)
        return self.configs_dict

    def get_yaml_from_configs_dict(self):
        ruamel.yaml.round_trip_dump(self.configs_dict, open(self.output_yaml_path, "w"), default_flow_style=False)
