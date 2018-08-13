import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("python", "2.7"),
    ("jfrog-artifactory-oss", ""),
    ("mysql-server", "5.7"),
    ("apache2", "2.4"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

    if pkg.version.strip():
        assert pkg.version.startswith(version)


@pytest.mark.parametrize("name", [
    "artifactory",
    "mysql",
    "apache2"
])
def test_services(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("username", [
    "artifactory",
    "mysql",
    "www-data"
])
def test_users(host, username):
    assert host.user(username).exists


def test_apache2_is_listening(host):
    assert host.socket('tcp://0.0.0.0:80').is_listening


def test_artifactory_is_listening(host):
    assert host.socket('tcp://0.0.0.0:8019').is_listening


def test_artifactory_is_up(host):
    html = host.command.check_output('curl -L -k http://localhost:80')
    assert 'artifactory' in html


def test_default_settings(host):
    artifactory_defaults = host.file('/etc/opt/jfrog/artifactory/default')
    assert artifactory_defaults.contains('-Xms512m')
    assert artifactory_defaults.contains('-Xmx2g')


def test_jmx_settings(host):
    artifactory_defaults = host.file('/etc/opt/jfrog/artifactory/default')
    assert artifactory_defaults.contains('export JAVA_OPTIONS="$JAVA_OPTIONS -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.rmi.port=9011 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=')
