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

class ProbabilisticMultipathTopo(Topo):

    def __init__(self, sw_path, thrift_port, pcap_dump, **opts):
        Topo.__init__(self, **opts)
        self.add_switches(sw_path, thrift_port, pcap_dump, **opts)
        self.add_hosts()
        self.add_links()

    def add_switches(self, sw_path, thrift_port, pcap_dump, **opts):
        self.networkSwitches = []
        self.networkSwitches.extend((
            self.addSwitch('s1', sw_path = sw_path, json_path = 'build/multipath_switch/multipath-switch.json', thrift_port = 9090, pcap_dump = pcap_dump),
            self.addSwitch('s2', sw_path = sw_path, json_path = 'build/dummy_switch/dummy-switch.json', thrift_port = 9091, pcap_dump = pcap_dump),
            self.addSwitch('s3', sw_path = sw_path, json_path = 'build/dummy_switch/dummy-switch.json', thrift_port = 9092, pcap_dump = pcap_dump),
            self.addSwitch('s4', sw_path = sw_path, json_path = 'build/dummy_switch/dummy-switch.json', thrift_port = 9093, pcap_dump = pcap_dump),
            self.addSwitch('s5', sw_path = sw_path, json_path = 'build/multipath_switch/multipath-switch.json', thrift_port = 9094, pcap_dump = pcap_dump)
        ))

    def add_hosts(self):
        self.networkHosts = []
        self.networkHosts.extend((
            self.addHost('h1', ip = '10.0.0.10/24', mac = '00:04:00:00:00:00'),
            self.addHost('h2', ip = '10.0.1.10/24', mac = '00:04:00:00:00:01'),
            self.addHost('h3', ip = '10.0.2.10/24', mac = '00:04:00:00:00:02'),
            self.addHost('h4', ip = '10.0.3.10/24', mac = '00:04:00:00:00:03')
        ))

    def add_links(self):
        self.addLink(self.networkHosts[0], self.networkSwitches[0])
        print('h1 -> s1', self.port('h1', 's1'))
        self.addLink(self.networkHosts[1], self.networkSwitches[0])
        print('h2 -> s1', self.port('h2', 's1'))

        self.addLink(self.networkSwitches[0], self.networkSwitches[1])
        print('s1 -> s2', self.port('s1', 's2'))
        self.addLink(self.networkSwitches[0], self.networkSwitches[2])
        print('s1 -> s3', self.port('s1', 's3'))
        self.addLink(self.networkSwitches[0], self.networkSwitches[3])
        print('s1 -> s4', self.port('s1', 's4'))

        self.addLink(self.networkSwitches[1], self.networkSwitches[4])
        print('s2 -> s5', self.port('s2', 's5'))
        self.addLink(self.networkSwitches[2], self.networkSwitches[4])
        print('s3 -> s5', self.port('s3', 's5'))
        self.addLink(self.networkSwitches[3], self.networkSwitches[4])
        print('s4 -> s5', self.port('s4', 's5'))

        self.addLink(self.networkHosts[2], self.networkSwitches[4])
        print('s5 -> h3', self.port('s5', 'h3'))
        self.addLink(self.networkHosts[3], self.networkSwitches[4])
        print('s5 -> h4', self.port('s5', 'h4'))

def get_args():
    parser = argparse.ArgumentParser(description='Mininet demo')
    parser.add_argument('--behavioral-exe', help='Path to behavioral model executable', type=str, action="store", required=True)
    parser.add_argument('--thrift-port', help='Thrift server port for table updates', type=int, action="store", default=9090)
    parser.add_argument('--json', help='Path to P4 JSON build file', type=str, action="store", required=True)
    parser.add_argument('--pcap-dump', help='Dump packets on interfaces to pcap files', type=str, action="store", required=False, default=False)
    return parser.parse_args()

def set_node_route(node, ip_addr, mac_addr, route_str):
    node.setARP(ip_addr, mac_addr)
    node.setDefaultRoute(route_str)

def initialize_routes(network):
    set_node_route(network.get('h1'), '10.0.0.1', '00:04:00:00:00:00', 'dev eth0 via 10.0.0.1')
    set_node_route(network.get('h2'), '10.0.1.1', '00:04:00:00:00:01', 'dev eth0 via 10.0.1.1')
    set_node_route(network.get('h3'), '10.0.2.1', '00:04:00:00:00:02', 'dev eth0 via 10.0.2.1')
    set_node_route(network.get('h4'), '10.0.3.1', '00:04:00:00:00:03', 'dev eth0 via 10.0.3.1')

def describe_hosts(network):
    host = network.get('h1')
    host.describe()
    host = network.get('h2')
    host.describe()
    host = network.get('h3')
    host.describe()
    host = network.get('h4')
    host.describe()

def run_network(network):
    sleep(1)
    print "Network Ready !"
    CLI(network)
    network.stop()

def main():
    args = get_args()
    topo = ProbabilisticMultipathTopo(args.behavioral_exe, args.thrift_port, args.pcap_dump)
    net = Mininet(topo = topo, host = P4Host, switch = P4Switch, controller = None)
    net.start()

    initialize_routes(net)
    describe_hosts(net)
    run_network(net)

if __name__ == '__main__':
    setLogLevel('info')
    main()