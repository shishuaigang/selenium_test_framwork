import os

import yaml


class ReadYaml:
    def __init__(self, yamlf):
        self.yamlf = yamlf

    def yaml_data(self):
        if os.path.exists(self.yamlf):
            with open(self.yamlf) as f:
                return yaml.load(f)
        else:
            raise FileNotFoundError('文件不存在')
