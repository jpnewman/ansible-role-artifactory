import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("python", "2.7"),
    ("jfrog-artifactory-oss", ""),
    ("apache2", "2.4"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

    if pkg.version.strip():
        assert pkg.version.startswith(version)


@pytest.mark.parametrize("name", [
    "mysql-server"
])
def test_no_packages(host, name):
    pkg = host.package(name)
    assert not pkg.is_installed


@pytest.mark.parametrize("name", [
    "artifactory",
    "apache2"
])
def test_services(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("name", [
    "mysql"
])
def test_no_services(host, name):
    service = host.service(name)
    assert not service.is_running
    assert not service.is_enabled


@pytest.mark.parametrize("username", [
    "artifactory",
    "www-data"
])
def test_users(host, username):
    assert host.user(username).exists


@pytest.mark.parametrize("username", [
    "mysql",
])
def test_no_users(host, username):
    assert not host.user(username).exists


def test_apache2_is_listening(host):
    assert host.socket('tcp://0.0.0.0:80').is_listening


def test_artifactory_is_listening(host):
    assert host.socket('tcp://0.0.0.0:8019').is_listening


def test_artifactory_is_up(host):
    html = host.command.check_output('curl -L -k http://localhost:80')
    assert 'artifactory' in html


def test_jmx_settings(host):
    artifactory_defaults = host.file('/etc/opt/jfrog/artifactory/default')
    assert artifactory_defaults.contains('export JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.rmi.port=9011 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=')
