import yaml
import logging

class YAMLWrapper:
    def __init__(self, data=None):
        self.data = data or {}

    @property
    def content(self):
        """返回当前的数据内容"""
        return self.data

    def load_yaml(self, yaml_file):
        """
        从YAML文件中加载数据。
        """
        try:
            with open(yaml_file, 'r') as file:
                self.data = yaml.safe_load(file)
            return self.data
        except FileNotFoundError:
            logging.error(f"Error: {yaml_file} not found.")
            return None
        except Exception as e:
            logging.error(f"An error occurred while reading the YAML file: {e}")
            return None

    def save_yaml(self, yaml_file):
        """
        将数据保存到YAML文件中。
        """
        try:
            with open(yaml_file, 'w') as file:
                yaml.safe_dump(self.data, file)
                return True
        except IOError as e:
            logging.error(f"An error occurred while saving the YAML file: {e}")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while saving the YAML file: {e}")
            return False


if __name__ == '__main__':
    data = {'users': [{'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
                      {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
                      {'id': 3, 'name': 'Bobc', 'email': 'bob@example1.com', 'age': 301}],
            'databases': [{'name': 'main_db', 'host': 'localhost', 'port': 5432},
                          {'name': 'backup_db', 'host': 'backup_server', 'port': 5432}]}
    yaml_wrapper = YAMLWrapper(data)
    yaml_file = 'E:\\AutomationApiTest_01\\Config\\config.yaml'
    print(yaml_wrapper.save_yaml(yaml_file))  # 加载YAML文件内容并打印
    print(yaml_wrapper.content)
