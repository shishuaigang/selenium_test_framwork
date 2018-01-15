import yaml
import os


class ReadYaml:
    def __init__(self, yamlf):
        self.yamlf = yamlf

    def yaml_data(self):
        if os.path.exists(self.yamlf):
            with open(self.yamlf) as f:
                return yaml.load(f)
        else:
            raise FileNotFoundError('文件不存在')


if __name__ == '__main__':
    data = ReadYaml(r'C:\Users\shishuaigang\Desktop\Important\selenium_test_framwork\config\config.yaml').yaml_data()
    print(data['URL'])
    print(os.path.abspath(__file__))
    print((os.path.dirname(os.path.abspath(__file__))))
    print(os.path.split(os.path.dirname(os.path.abspath(__file__))))
