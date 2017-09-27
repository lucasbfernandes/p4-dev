#include "includes/headers.p4"
#include "includes/parser.p4"

counter my_inner_switch_counter {
    type: packets;
    direct: forward;    
}

action set_destination(dmac, port) {
    modify_field(ethernet.dstAddr, dmac);
    modify_field(standard_metadata.egress_spec, port);
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
    apply(forward);
}

control egress {

}
