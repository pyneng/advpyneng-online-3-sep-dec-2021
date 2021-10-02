class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"
