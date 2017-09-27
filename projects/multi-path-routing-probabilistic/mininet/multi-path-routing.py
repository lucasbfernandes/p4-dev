import os
import sys
import argparse

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/mininet")

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from p4_mininet import P4Switch, P4Host
from time import sleep

NUM_HOSTS = 3

class MultipathRoutingTopo(Topo):

    def __init__(self, sw_path, json_path, thrift_port, pcap_dump, **opts):
        Topo.__init__(self, **opts)
        self.initialize_variables()
        self.add_switches(sw_path, json_path, thrift_port, pcap_dump, **opts)
        self.add_hosts(self.hostsCount)
        self.build_network_topo()

    def initialize_variables(self):
        self.networkSwitches = []
        self.networkHosts = []
        self.hostsCount = NUM_HOSTS

    def add_switches(self, sw_path, json_path, thrift_port, pcap_dump, **opts):
        self.networkSwitches.extend((
            self.addSwitch('s1', sw_path = sw_path, json_path = 'build/external_switch/external-switch.json', thrift_port = 9090, pcap_dump = pcap_dump),
            self.addSwitch('s2', sw_path = sw_path, json_path = 'build/inner_switch/inner-switch.json', thrift_port = 9091, pcap_dump = pcap_dump),
            self.addSwitch('s3', sw_path = sw_path, json_path = 'build/inner_switch/inner-switch.json', thrift_port = 9092, pcap_dump = pcap_dump),
            self.addSwitch('s4', sw_path = sw_path, json_path = 'build/external_switch/external-switch.json', thrift_port = 9093, pcap_dump = pcap_dump)
        ))

    def add_hosts(self, number):
        for i in xrange(number):
            host = self.addHost('h%d' % (i + 1), ip = '10.0.%d.10/24' % i, mac = '00:04:00:00:00:%02x' %i)
            self.networkHosts.append(host)

    def build_network_topo(self):
        self.addLink(self.networkHosts[0], self.networkSwitches[0])
        print('h1 <-> s1:')
        print(self.port(self.networkHosts[0], self.networkSwitches[0]))

        self.addLink(self.networkHosts[1], self.networkSwitches[0])
        print('h2 <-> s1:')
        print(self.port(self.networkHosts[1], self.networkSwitches[0]))

        self.addLink(self.networkSwitches[0], self.networkSwitches[1])
        print('s1 <-> s2:')
        print(self.port(self.networkSwitches[0], self.networkSwitches[1]))

        self.addLink(self.networkSwitches[0], self.networkSwitches[2])
        print('s1 <-> s3:')
        print(self.port(self.networkSwitches[0], self.networkSwitches[2]))

        self.addLink(self.networkSwitches[1], self.networkSwitches[3])
        print('s2 <-> s4:')
        print(self.port(self.networkSwitches[1], self.networkSwitches[3]))

        self.addLink(self.networkSwitches[2], self.networkSwitches[3])
        print('s3 <-> s4:')
        print(self.port(self.networkSwitches[2], self.networkSwitches[3]))

        self.addLink(self.networkSwitches[3], self.networkHosts[2])
        print('s4 <-> h3:')
        print(self.port(self.networkSwitches[3], self.networkHosts[2]))

def get_args():
    parser = argparse.ArgumentParser(description='Mininet demo')
    parser.add_argument('--behavioral-exe', help='Path to behavioral model executable', type=str, action="store", required=True)
    parser.add_argument('--thrift-port', help='Thrift server port for table updates', type=int, action="store", default=9090)
    parser.add_argument('--mode', choices=['l2', 'l3'], type=str, default='l3')
    parser.add_argument('--json', help='Path to JSON config file', type=str, action="store", required=True)
    parser.add_argument('--pcap-dump', help='Dump packets on interfaces to pcap files', type=str, action="store", required=False, default=False)
    return parser.parse_args()

def set_node_route(node, ip_addr, mac_addr, route_str):
    node.setARP(ip_addr, mac_addr)
    node.setDefaultRoute(route_str)

def initialize_routes(network):
    set_node_route(network.get('h1'), '10.0.0.1', '00:04:00:00:00:00', 'dev eth0 via 10.0.0.1')
    set_node_route(network.get('h2'), '10.0.1.1', '00:04:00:00:00:01', 'dev eth0 via 10.0.1.1')
    set_node_route(network.get('h3'), '10.0.2.1', '00:04:00:00:00:02', 'dev eth0 via 10.0.2.1')

def describe_hosts(network):
    for i in xrange(NUM_HOSTS):
        host = network.get('h%d' % (i + 1))
        host.describe()

def run_network(network):
    sleep(1)
    print "Ready !"
    CLI(network)
    network.stop()

def main():
    args = get_args()
    mode = args.mode
    topo = MultipathRoutingTopo(args.behavioral_exe, args.json, args.thrift_port, args.pcap_dump)
    net = Mininet(topo = topo, host = P4Host, switch = P4Switch, controller = None)
    net.start()

    initialize_routes(net)
    describe_hosts(net)
    run_network(net)

if __name__ == '__main__':
    setLogLevel('info')
    main()