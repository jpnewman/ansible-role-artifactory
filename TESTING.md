
# Testing

## Setup Environment

~~~
virtualenv --no-site-packages .venv
~~~

~~~
source .venv/bin/activate
~~~

## Install Dependencies

~~~
pip install -r requirements.txt
~~~

### VirtualBox

> Mac OS X

~~~
brew cask install virtualbox
brew cask install virtualbox-extension-pack
~~~

### Vagrant

> Mac OS X

~~~
brew cask install vagrant
~~~

### Vagrant-Manager

> Mac OS X

~~~
brew cask install vagrant-manager
~~~

## Running Tests

### All Platforms

~~~
molecule test
~~~

~~~
unbuffer molecule test | tee >(ansi2html > molecule.html)
~~~

### Debug, don't destroy

~~~
molecule --debug test --destroy=never
~~~

### Specific Scenario

~~~
molecule test --scenario-name=xenial64_derby
molecule test --scenario-name=centos7_derby
~~~

~~~
unbuffer molecule test --scenario-name=xenial64_derby | tee >(ansi2html > xenial64_derby.html)
~~~

### Login

~~~
molecule login --host ansible-role-artifactory-trusty64
molecule login --host ansible-role-artifactory-xenial64
molecule login --host ansible-role-artifactory-jessie64
molecule login --host ansible-role-artifactory-stretch64
~~~

## Destroy, All Platforms

~~~
molecule destroy
~~~
