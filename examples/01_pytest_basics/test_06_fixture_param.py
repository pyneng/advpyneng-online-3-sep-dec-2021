from pprint import pprint
import pytest
import yaml
from netmiko import ConnectHandler


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
# pprint(devices)
[
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "password": "cisco",
        "secret": "cisco",
        "username": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.2",
        "password": "cisco",
        "secret": "cisco",
        "username": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.3",
        "password": "cisco",
        "secret": "cisco",
        "username": "cisco",
    },
]


@pytest.fixture(params=devices)
def ssh_connection(request):
    ssh = ConnectHandler(**request.param)
    ssh.enable()
    yield ssh
    ssh.disconnect()


def test_ospf(ssh_connection):
    output = ssh_connection.send_command("sh ip ospf")
    assert "routing process" in output.lower()


def test_loopback(ssh_connection):
    loopback = "Loopback0"
    output = ssh_connection.send_command("sh ip int br")
    assert loopback in output


# @pytest.fixture(
#     params=["192.168.100.1", "192.168.100.2", "192.168.100.3"],
#     scope="module",
# )
# def ssh_conn(request):
#     #print("\n\n>>> SETUP", request.param)
#     device = {
#         "host": request.param,
#         "device_type": "cisco_ios",
#         "password": "cisco",
#         "secret": "cisco",
#         "username": "cisco",
#     }
#     with ConnectHandler(**device) as ssh:
#         ssh.enable()
#         yield ssh
#     #print("\n\n<<< TEARDOWN", request.param)
# 
# 
