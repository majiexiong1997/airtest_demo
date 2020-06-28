from airtest.core.api import *
from airtest.core.api import connect_device
from center.main_page import MainPage
from airtest.core.android.adb import *
class adb_collect:
    def __init__(self,):
        self.phone_size = []
    def get_phone_size(self,device):
        get_device = device.adb.get_device_info()
        # get_model = device.adb.get_model()  #手机型号
        get_ip = device.adb.get_ip_address()  #手机地址
        # get_memory = device.adb.get_memory()  # 手机内存
        # get_gpu = device.adb.get_gpu()  # 手机GPU
        # get_cpuabi = device.adb.get_cpuabi() #cpu型号
        # get_cpufreq = device.adb.get_cpufreq()  # cpu频率
        # get_cpuinfo = device.adb.get_cpuinfo()  # cpu 核数
        # get_storage = device.adb.get_storage()  #手机内存
        self.phone_size.append(get_device['model'])
        self.phone_size.append(get_device['manufacturer'])
        self.phone_size.append(get_ip)
        self.phone_size.append(get_device['memory'])
        self.phone_size.append(get_device['gpu']['gpuModel'])
        self.phone_size.append(get_device['cpuabi'])
        self.phone_size.append(get_device['cpufreq'])
        self.phone_size.append(get_device['cpuinfo']['cpuNum'])
        self.phone_size.append(get_device['storage'])
        return self.phone_size
    def install_app(self,device):
        package = MainPage.main_package
        device.check_app(package)


class adb(ADB):
    def check_app(self, package):
        output = self.shell(['dumpsys', 'package', package])
        pattern = r'Package\s+\[' + str(package) + '\]'
        match = re.search(pattern, output)
        if match is None:
            return False
        return True
    def get_storage(self):
        res = self.shell("df /data")
        pat = re.compile(r".*\/data\s+(\S+)", re.DOTALL)
        if pat.match(res):
            _str = pat.match(res).group(1)
        else:
            pat = re.compile(r".*\s+(\S+)\s+\S+\s+\S+\s+\S+\s+\/data", re.DOTALL)
            _str = pat.match(res).group(1)
        if 'G' in _str:
            _num = round(float(_str[:-1]))
        elif 'M' in _str:
            _num = round(float(_str[:-1]) / 1000.0)
        else:
            _num = round(float(_str) / 1000.0 / 1000.0)
        if _num > 512:
            res = '1T'
        elif _num > 256:
            res = '512G'
        elif _num > 128:
            res = '256G'
        elif _num > 64:
            res = '128G'
        elif _num > 32:
            res = '64G'
        elif _num > 16:
            res = '32G'
        elif _num > 8:
            res = '16G'
        else:
            res = '8G'
        return res











