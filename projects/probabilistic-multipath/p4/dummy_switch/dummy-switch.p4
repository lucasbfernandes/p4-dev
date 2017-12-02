#include "includes/headers.p4"
#include "includes/parser.p4"

counter dummy_switch_counter {
    type: packets;
    static: process_path;
    instance_count: 8;
}

action count_path(path) {
    count(dummy_switch_counter, path);
}

action set_destination(dmac, port) {
    modify_field(ethernet.dstAddr, dmac);
    modify_field(standard_metadata.egress_spec, port);
}

table process_path {
    reads {
        ipv4.srcAddr : exact;
        ipv4.dstAddr : exact;
    }
    actions {
        count_path;
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
    apply(process_path);
    apply(forward);
}

control egress {

}
