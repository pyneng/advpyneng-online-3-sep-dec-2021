import pytest
from netmiko import Netmiko



@pytest.fixture(scope="session")
def cisco_ios_router_common_params():
    data = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    return data


@pytest.fixture(scope="session")
def cisco_ios_router_reachable():
    data = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    return data


@pytest.fixture(scope="session")
def ssh_connection_cisco_ios(cisco_ios_router_reachable):
    print("\n### SETUP\n")
    ssh = Netmiko(**cisco_ios_router_reachable)
    ssh.enable()
    yield ssh
    ssh.disconnect()
    print("\n### TEARDOWN\n")
