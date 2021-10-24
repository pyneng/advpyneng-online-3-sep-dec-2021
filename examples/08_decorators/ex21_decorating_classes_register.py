class CiscoIosBase:
    pass


class CiscoSSH(CiscoIosBase):
    device_type = "cisco_ios"

    def __init__(self, ip, user, password):
        pass


class JuniperSSH:
    device_type = "juniper"

    def __init__(self, ip, user, password):
        pass
