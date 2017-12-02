#include "includes/headers.p4"
#include "includes/parser.p4"

counter dummy_switch_counter {
    type: packets;
    static: process_port;
    instance_count: 10; 
}

action count_port(port) {
    count(dummy_switch_counter, port);
}

action set_destination(dmac, port) {
    modify_field(ethernet.dstAddr, dmac);
    modify_field(standard_metadata.egress_spec, port);
}

table process_port {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        count_port;
    }
}

table forward {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_destination;
    }
}

control ingress {
    apply(process_port);
    apply(forward);
}

control egress {

}
