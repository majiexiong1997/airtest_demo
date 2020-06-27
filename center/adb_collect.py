from airtest.core.api import *
from airtest.core.api import connect_device

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
    def wait(self):
        pass







