# direct_flow_counter

## Description

P4 example program that implements a simple forwarding mechanism between two hosts and a switch. The following image might help to understand how the network topology was planned:
<br>
<br>
<p align="center">
  <img src="https://github.com/lucasbfernandes/p4-dev/blob/master/projects/direct_flow_counter/images/direct_flow_counter.png?raw=true"     alt="Network topology"/>
</p>

There are two hosts (h1, h2) connected by a single switch (s1), where packets coming from h1 pass through switch port number 1 and packets from h2 pass through port number 2.
<br>
<br>
The entries added to the switch were:

    $ table_add forward set_destination 10.0.0.10 => 00:04:00:00:00:00 1
    $ table_add forward set_destination 10.0.1.10 => 00:04:00:00:00:01 2

The first entry says that packets going to ip 10.0.0.10 (h1) must be forwarded to a host with mac address 00:04:00:00:00:00 and must pass through switch port number 1. The second line is doing the same but for packets going to ip 10.0.1.10 (h2).
<br>
<br>
Another feature that was implemented in this project is a counter for each of the forward table entries. Everytime an incoming packet matches a forward table entry (i.e. everytime a packet is being sent to one of the ips above) the counter is incremented.

## Usage

From the root of this project, type:

    $ python tools/build_project.py #will compile the p4 program and generate a json representation
    $ python tools/run_project.py #will initialize a mininet network with the specified topology

In another terminal window, type:
  
    $ python tools/apply_commands.py #will apply commands defined in util/commands.txt
    $ python tools/run_cli.py #will run an interactive shell for custom commands
    
If you wish to test network reachability, go to the first terminal window and type:

    $ h1 ping -c 2 h2 #will send two packets from h1 to h2

If you wish to check the counter values, go to the second terminal window and type:

    $ counter_read my_direct_counter 0 #for entry 1
    $ counter_read my_direct_counter 1 #for entry 2
