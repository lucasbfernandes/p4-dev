#include "includes/headers.p4"
#include "includes/parser.p4"

counter my_static_counter {
    type: packets;
    static: forward;
    instance_count: 1;
}

action _drop() {
    count(my_static_counter, 0);
    drop();
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
        _drop;
    }
}

control ingress {
    apply(forward);
}

control egress {

}
