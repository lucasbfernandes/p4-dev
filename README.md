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

### Floodlight

	$ cd git_modules/floodlight
	$ git submodule init
	$ git submodule update
	$ ant

	$ sudo mkdir /var/lib/floodlight
	$ sudo chmod 777 /var/lib/floodlight

## Future Work

* Automate installation process.