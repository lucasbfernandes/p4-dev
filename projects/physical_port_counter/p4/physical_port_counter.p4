#include "includes/headers.p4"
#include "includes/parser.p4"

counter my_static_counter {
    type: packets;
    static: process_port;
    instance_count: 1; 
}

action count_port() {
    count(my_static_counter, 0);
}

action set_destination(dmac, port) {
    modify_field(ethernet.dstAddr, dmac);
    modify_field(standard_metadata.egress_spec, port);
}

table process_port {
    reads {
        standard_metadata.ingress_port : exact;
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
