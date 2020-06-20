import yaml


class yaml_load(object):
    '''文件读取'''

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        try:
            self.f = open(self.yaml_file, 'rb')
            self.cfg = self.f.read()
        except FileNotFoundError:
            print(f'{self.yaml_file}文件不存在{FileNotFoundError}')

    def load_yaml(self):
        all_data = yaml.safe_load(self.cfg)



class yaml_dump(object):
    # 文件写入
    def __init__(self):
        pass

    def dump_yaml(self, filepath, data, mode='w'):
        try:
            with open(filepath, mode) as f:
                yaml.safe_dump(data, f)
                print(F'内容{data}\n写入{filepath}成功')
            return True
        except Exception as e:
            print(F'内容{data}\n写入{filepath}文件出错，错误{e}')
            return False
