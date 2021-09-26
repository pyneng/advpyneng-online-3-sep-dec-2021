import subprocess
import pytest
from netmiko import ConnectHandler
import re
import yaml


with open("devices.yaml") as f:
    devices_params = yaml.safe_load(f)
ip_list = [d["host"] for d in devices_params]


@pytest.fixture(params=devices_params, scope="session", ids=ip_list)
def ssh_connection(request):
    ssh = ConnectHandler(**request.param)
    ssh.enable()
    # print(f"\n\n>>>>> Подключение {request.param['host']}")
    yield ssh
    # print(f"\n\n>>>>> Закрываю сессию {request.param['host']}")
    ssh.disconnect()


@pytest.mark.parametrize(
    "ip",
    ["192.168.100.100", "192.168.100.2", "192.168.100.3"],
    ids=["ISP1", "ISP2", "FW"],
)
def test_ping(ssh_connection, ip):
    output = ssh_connection.send_command(f"ping {ip}")
    assert "success rate is 100 percent" in output.lower()


def test_ospf_enabled(ssh_connection):
    output = ssh_connection.send_command("sh ip ospf")
    assert "routing process" in output.lower()


def test_loopback(ssh_connection):
    output = ssh_connection.send_command("sh ip int br | i up +up")
    # assert "Loopback0" in output
    assert "Loopback0" in parse_sh_ip_int_br(output)
