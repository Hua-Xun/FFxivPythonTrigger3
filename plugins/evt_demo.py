import re
from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.decorator import event


class EvtDemo(PluginBase):
    name = "EvtDemo"

    @event("log_event")
    def log_event(self, evt):
        if re.search(r'地下\d+0层', evt.message):
            self.logger("123142123123")
            plugins.XivHacks.moving_z_modify = 0  # 将遁地数值设定为0
        if re.search(r'第\d+0层', evt.message):
            self.logger("123")
            plugins.XivHacks.moving_z_modify = 0  # 将遁地数值设定为0
        if re.search(r'进入了休息区', evt.message):
            self.logger("250")
            plugins.XivHacks.moving_z_modify = 0  # 将遁地数值设定为0
            plugins.XivHacks.speed_percent = 1.05 #将速度数值设定为1.05
