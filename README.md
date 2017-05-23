# p4-dev
Workspace for p4 related development.

## Installation

### Behavioral Model

	$ cd git_modules/bmv2
	$ ./install_deps.sh
	$ ./autogen.sh
	$ ./configure
	$ make
	$ sudo make install

### p4c-bm

	$ cd git_modules/p4c-bm
	$ sudo pip install -r requirements.txt
	$ sudo python setup.py install

### Floodlight

	$ cd git_modules/floodlight
	$ git submodule init
	$ git submodule update
	$ ant
	$ sudo mkdir /var/lib/floodlight
	$ sudo chmod 777 /var/lib/floodlight

## Future Work

* Automate installation process.