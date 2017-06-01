# physical_port_counter

## Description

P4 example program that implements a simple forwarding mechanism between three hosts and a switch. The following image might help to understand how the network topology was planned:
<br>
<br>
<p align="center">
  <img src="https://github.com/lucasbfernandes/p4-dev/blob/master/projects/physical_port_counter/images/physical_port_counter.png?raw=true"     alt="Network topology"/>
</p>

There are three hosts (h1, h2, h3) connected by a single switch (s1), where packets coming from h1 pass through switch port number 1, packets from h2 pass through port number 2 and packets from h3 pass through port number 3.
<br>
<br>
The entries added to the switch were:

    $ table_add process_port count_port 1 =>
    $ table_add forward set_destination 10.0.0.10 => 00:04:00:00:00:00 1
    $ table_add forward set_destination 10.0.1.10 => 00:04:00:00:00:01 2
    $ table_add forward set_destination 10.0.2.10 => 00:04:00:00:00:02 3

The first entry says that every packet entering the switch from physical port number 1 must be accounted for. The p4 action that is implementing it can be easily found in this project.
<br>
<br>
The second entry says that packets going to ip 10.0.0.10 (h1) must be forwarded to a host with mac address 00:04:00:00:00:00 and must pass through switch port number 1. The second line and third line are doing the same but for packets going to ip 10.0.1.10 (h2) and 10.0.2.10 (h3).
<br>
<br>
There is a counter dedicated to accounting packets entering the switch from port number 1. It is called my_static_counter and can be read from the project CLI.

## Usage

From the root of this project, type:

    $ python tools/build_project.py #will compile the p4 program and generate a json representation
    $ python tools/run_project.py #will initialize a mininet network with the specified topology

In another terminal window, type:
  
    $ python tools/apply_commands.py #will apply commands defined in util/commands.txt
    $ python tools/run_cli.py #will run an interactive shell for custom commands
    
If you wish to test network reachability, go to the first terminal window and type:

    $ h1 ping -c 2 h2 #will send two packets from h1 to h2
    $ h1 ping -c 2 h3 #will send two packets from h1 to h3
    $ h2 ping -c 2 h3 #will send two packets from h2 to h3

If you wish to check the counter value, go to the second terminal window and type:

    $ counter_read my_static_counter 0 #will read the port 1 counter
