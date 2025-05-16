import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")

@pytest.mark.parametrize(
    "directory",
    [
        "/opt/teku/data",
        "/opt/teku/config",
        "/opt/teku/logs",
        "/opt/teku/lib",
    ]
)
def test_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "teku"
    assert d.group == "teku"

@pytest.mark.parametrize(
    "file",
    [
        "/usr/local/bin/teku",
        "/etc/systemd/system/teku.service",
        "/opt/teku/config/config.yaml"
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file

@pytest.mark.parametrize("service", ["teku"])
def test_service(host, service):
    s = host.service(service)
    assert s.is_running
    assert s.is_enabled


@pytest.mark.parametrize("socket", ["tcp://127.0.0.1:8008", "tcp://127.0.0.1:8551"])
def test_socket(host, socket):
    s = host.socket(socket)
    assert s.is_listening


@pytest.mark.parametrize("command", ["curl -s http://127.0.0.1:8551/eth/v1/node/identity"])
def test_port(host, command):
    c = host.run(command)
    assert c.stderr == ""
    assert c.succeeded
