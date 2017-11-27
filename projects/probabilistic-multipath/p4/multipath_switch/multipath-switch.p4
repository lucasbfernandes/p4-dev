#include "includes/headers.p4"
#include "includes/parser.p4"

field_list multi_path_hash_fields {
    meta.meta_handle;
}

field_list_calculation multi_path_port_selector {
    input {
        multi_path_hash_fields;
    }
    algorithm : multi_path_probability_hash;
    output_width: 32;
}

action_selector multi_path_action_selector {
    selection_key : multi_path_port_selector;
}

action _nop() {

}

action set_multi_path_destination(port) {
    modify_field(standard_metadata.egress_spec, port);
}

action_profile probability_multipath_profile {
    actions {
        _nop;
        set_multi_path_destination;
    }
    size : 64;
    dynamic_action_selection : multi_path_action_selector;
}

table multi_path_profile_forward {
    reads {
        ipv4.dstAddr : exact;
    }
    action_profile: probability_multipath_profile;
    size : 1024;
}

table multi_path_regular_forward {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_multi_path_destination;
    }
}

action set_meta_handle(port) {
    modify_field(meta.meta_handle, port);
}

table multi_path_compute_meta {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_meta_handle;
    }
}

action set_dmac(dmac) {
    modify_field(ethernet.dstAddr, dmac);
}

table multi_path_set_dmac {
    reads {
        ipv4.dstAddr : exact;
    }
    actions {
        set_dmac;
    }
}

control ingress {
    apply(multi_path_compute_meta);
    apply(multi_path_set_dmac);
    apply(multi_path_regular_forward);
    apply(multi_path_profile_forward);
}

control egress {

}
