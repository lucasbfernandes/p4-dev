#include "includes/headers.p4"
#include "includes/parser.p4"

field_list mp_hash_fields {
    ipv4.srcAddr;
    ipv4.dstAddr;
    ipv4.totalLen;
    meta.maxflow_handle;
    meta.probability_handle;
}

field_list_calculation mp_port_selector {
    input {
        mp_hash_fields;
    }
    algorithm : probabilistic_simple_multipath;
    output_width: 32;
}

action_selector mp_action_selector {
    selection_key : mp_port_selector;
}

action _nop() {

}

action set_mp_port(port) {
    modify_field(standard_metadata.egress_spec, port);
}

action_profile mp_profile {
    actions {
        _nop;
        set_mp_port;
    }
    size : 64;
    dynamic_action_selection : mp_action_selector;
}

table mp_profile_forward {
    reads {
        ipv4.srcAddr : exact;
        ipv4.dstAddr : exact;
    }
    action_profile: mp_profile;
    size : 1024;
}

table mp_regular_forward {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_mp_port;
    }
}

action set_probability_handle(port) {
    modify_field(meta.probability_handle, port);
}

table mp_probability_meta {
    reads {
        ipv4.srcAddr : exact;
        ipv4.dstAddr : exact;
    }
    actions {
        set_probability_handle;
    }
}

action set_maxflow_handle(port) {
    modify_field(meta.maxflow_handle, port);
}

table mp_maxflow_meta {
    reads {
        ipv4.srcAddr : exact;
        ipv4.dstAddr : exact;
    }
    actions {
        set_probability_handle;
    }
}

action set_dmac(dmac) {
    modify_field(ethernet.dstAddr, dmac);
}

table mp_set_dmac {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_dmac;
    }
}

counter path_counter {
    type: packets;
    static: mp_count_path;
    instance_count: 8;
}

action count_path(path) {
    count(path_counter, path);
}

action set_destination(dmac, port) {
    modify_field(ethernet.dstAddr, dmac);
    modify_field(standard_metadata.egress_spec, port);
}

table mp_count_path {
    reads {
        ipv4.srcAddr : exact;
        ipv4.dstAddr : exact;
    }
    actions {
        count_path;
    }
}

table mp_forward {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_destination;
    }
}

control ingress {
    apply(mp_probability_meta);
    apply(mp_maxflow_meta);
    apply(mp_set_dmac);
    apply(mp_regular_forward);
    apply(mp_profile_forward);
    apply(mp_count_path);
    apply(mp_forward);
}

control egress {

}
