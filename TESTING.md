
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

### Specific Platform

~~~
molecule test --platform=trusty64
molecule test --platform=xenial64
molecule test --platform=jessie64
molecule test --platform=stretch64
~~~

### Login

~~~
molecule login --host ansible-role-java-trusty64
molecule login --host ansible-role-java-xenial64
molecule login --host ansible-role-java-jessie64
molecule login --host ansible-role-java-stretch64
~~~

## Destroy, All Platforms

~~~
molecule destroy
~~~
