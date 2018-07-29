# jpnewman.artifactory

[![Ansible Role](https://img.shields.io/ansible/role/12824.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/artifactory/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-artifactory.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-artifactory)

This is an Ansible role to install artifactory.

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|:--|
|**defaults jpnewman.artifactory**|||
|```artifactory_type```|```oss``` or ```pro```|```oss```|
|```artifactory_home```||/var/opt/jfrog/artifactory|
|```artifactory_default_file```||/etc/opt/jfrog/artifactory/default|
|```artifactory_license_file```|||
|```artifactory_license_path```||"/etc/opt/jfrog/artifactory/artifactory.lic"|
|```artifactory_service_name```||artifactory|
|**Derby Database / Derby Tools**|||
|```artifactory_derby_tools_install```||false|
|```artifactory_derby_tools_version```||10.12.1.1|
|```artifactory_derby_tools_url```||"http://apache.mirror.anlx.net//db/derby/db-derby-{{ artifactory\_derby\_tools\_version }}/db-derby-{{ artifactory\_derby\_tools\_version }}-bin.zip"|
|**MySQL**|||
|```artifactory_database```||See sections ```artifactory_database_object_derby``` and ```artifactory_database_object``` below.|
|**JDBC Connector-J**|||
|```artifactory_database_file_title```||mysql-connector-java-5.1.44|
|```artifactory_database_jdbc_url```||"http://dev.mysql.com/get/Downloads/Connector-J/{{ artifactory\_database\_file\_title }}.tar.gz"|
|```artifactory_database_filename```||```{{ artifactory_database_file_title }}.jar```|
|**geerlingguy.mysql**|||
|```mysql_innodb_file_per_table```||"1"|
|```mysql_innodb_buffer_pool_size```||1536M|
|```mysql_tmp_table_size```||512M|
|```mysql_max_heap_table_size```||512M|
|```mysql_innodb_log_file_size```||256M|
|```mysql_innodb_log_buffer_size```||4M|
|**Reverse Proxy**|||
|```artifactory_proxy```||apache / nginx|
|**JMX**|||
|```artifactory_jmx_enable```||true|
|```artifactory_jmx_java_options```||'export JAVA\_OPTIONS="$JAVA\_OPTIONS -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.rmi.port=9011 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname={{ ansible_hostname }}"'|
|```artifactory_jmx_jmxterm_install```||true|
|```artifactory_jmx_jmxterm_url```||https://downloads.sourceforge.net/project/cyclops-group/jmxterm/1.0.0/jmxterm-1.0.0-uber.jar|
|**Encryption**|||
|```artifactory_api_username```|Artifactory API username||
|```artifactory_api_password```|Artifactory API password||
|```artifactory_api_url```|Artifactory API URL||
|```change_existing_artifactory_db_properties```|Change Existing Artifactory db.properties|true|

## ```artifactory_database_object_derby```

To configure a Derby database define the following variables for ```artifactory_database```: -

|Variable|Description|Default|
|---|---|:--|
|```type```|Derby / MySQL / PostgreSQL|Derby|
|```url```||jdbc:derby:{db.home};create=true|
|```driver```||org.apache.derby.jdbc.EmbeddedDriver|

## ```artifactory_database_object_mysql```

To configure a MySQL database define the following variables for ```artifactory_database```: -

|Variable|Description|Default|
|---|---|:--|
|```type```||mysql|
|```driver```||com.mysql.jdbc.Driver|
|```url```||'jdbc:mysql://localhost:3306/artdb?characterEncoding=UTF-8&elideSetAutoCommits=true'|
|```username```||artifactory|
|```password```||password|
|```database```||artdb|

## NOTES

Review ```TODO.md``` for information on outstanding items, like ```nginx``` reverse proxy support.

## Encryption

Artifactory encrypts passwords in configuration files.

If the following variables are defined the password will be decrypted when the templates are compared: -

|Variable|Description|
|---|---|
|```artifactory_api_username```|Artifactory API username|
|```artifactory_api_password```|Artifactory API password|
|```artifactory_api_url```|Artifactory API URL|

These are used for the API ```/api/system/decrypt``` and ```/api/system/encrypt``` commands and help make the role idempotent.

<https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ActivateMasterKeyEncryption>

## Tuning MySQL

- <https://www.jfrog.com/confluence/display/RTF/MySQL>

Create a variable file named ```geerlingguy.mysql.yml``` with the following content and place it in either ```host_vars``` or ```group_vars``` folder.

~~~
---

mysql_innodb_file_per_table: "1"

mysql_innodb_buffer_pool_size: 1536M
mysql_tmp_table_size: 512M
mysql_max_heap_table_size: 512M

mysql_innodb_log_file_size: 256M
mysql_innodb_log_buffer_size: 4M
~~~

## JMX Connection

> Connection String

~~~
service:jmx:rmi://<pub-ip>:<rmi-port>/jndi/rmi://<pub-ip>:<registry-port>/jmxrmi
~~~

> JConsole

~~~
JConsole service:jmx:rmi://artifactory-server:9011/jndi/rmi://artifactory-server:9010/jmxrmi
~~~

> JMXTerms

~~~
java -jar jmxterm.jar -l "service:jmx:rmi://artifactory-server:9011/jndi/rmi://artifactory-server:9010/jmxrmi"
~~~

## License

MIT / BSD

## Author Information

John Paul Newman
