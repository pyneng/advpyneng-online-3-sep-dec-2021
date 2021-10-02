import time


class BaseSSH:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        for command in commands:
            time.sleep(0.5)
        return "result"


class CiscoSSH(BaseSSH):
    def __init__(self, ip, username, password, secret, disable_paging=True):
        super().__init__(ip, username, password)

    def send_config_commands(self, commands):
        # send....(conf t)
        return "result"
