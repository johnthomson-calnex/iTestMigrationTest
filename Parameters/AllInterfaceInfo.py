#####################################################################
#                                                                   #
#   This file contains functions corresponding to each interface    #
#   each function will have the data relevant to the interface      #
#   such as te midpoint values and tolerances.                      #
#                                                                   #
#####################################################################
def rj45_lowrate_100m():
    return {
        'linerate' : '100M',
        'interface'  :'RJ45LowRate',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 20339.609,
        't4_midpoint_nrz_nib' : 20339.609,
        't4_midpoint_pam4_nib' : 20339.609,
        'tolerance' : 10,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 10,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 10,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 10,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 10,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 20,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 10

    }

def sfp100m():
    return {
        'linerate' : '100G',            
        'interface'  :'SFP100M',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 20247.385,
        't4_midpoint_nrz_nib' : 20247.385,
        't4_midpoint_pam4_nib' : 20247.385,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }

def rj45_lowrate_1g():
    return {
        'linerate' : '1G',
        'interface'  :'RJ45LowRate',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 7099.468,
        't4_midpoint_nrz_nib' : 7099.468,
        't4_midpoint_pam4_nib' : 7099.468,
        'tolerance' : 15,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 15,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 15,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 15,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 15,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' :30,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 15

    }

def sfp1g():
    return {
        'linerate' : '1G',
        'interface'  :'SFP1G',
        'fec_status' : 'false',
        'flexe_status' : '',
        'full_interface_name' : 'SFP1G',
        't4_midpoint_nrz_jib' : 7086.628,
        't4_midpoint_nrz_nib' : 7086.628,
        't4_midpoint_pam4' : 7086.628,
        't4_midpoint_pam4_nib_legacy' : 7094.628,
        'tolerance' : 1.5,

        'fec_possible'  :False,
        'flexe_possible'  :False,
        'default_linerate' : True,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def sfpplus():
    return {
        'linerate' : '10G',
        'interface'  :'SFPPLUS',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 52192.455,
        't4_midpoint_nrz_nib' : 52192.455,
        't4_midpoint_pam4_nib' : 52192.455,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def sfp28_25g():
    return {
        'linerate' : '25G',
        'interface'  :'SFP28',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 21760.442,
        't4_midpoint_nrz_nib' : 21760.442,
        't4_midpoint_pam4_nib' : 21760.442,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def sfp28_25g_fec():
    return {
        'linerate' : '25G',
        'interface'  :'SFP28',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 21892.811,
        't4_midpoint_nrz_nib' : 21892.811,
        't4_midpoint_pam4_nib' : 21892.811,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfpplus():
    return {
        'linerate' : '40G',
        'interface'  :'QSFPPLUS',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 13977.7,
        't4_midpoint_nrz_nib' : 13977.7,
        't4_midpoint_pam4_nib' : 13977.7,
        't4_midpoint_nrz_jib_legacy' : 13977.7,
        't4_midpoint_nrz_nib_legacy' : 13977.7,
        't4_midpoint_pam4_nib_legacy' : 13977.7,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_50g_01():
    return {
        'linerate' : '50GLanes0',              
        'interface'  :'QSFP28',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 11481.492,
        't4_midpoint_nrz_nib' : 11481.492,
        't4_midpoint_pam4_nib' : 11481.492,
        't4_midpoint_nrz_jib_legacy' : 11481.492,
        't4_midpoint_nrz_nib_legacy' : 11481.492,
        't4_midpoint_pam4_nib_legacy' : 11481.492,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_50g_01_fec():
    return {
        'linerate' : '50GLanes0',              
        'interface'  :'QSFP28',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 11824.122,
        't4_midpoint_nrz_nib' : 11824.122,
        't4_midpoint_pam4_nib' : 11824.122,
        't4_midpoint_nrz_jib_legacy' : 11824.122,
        't4_midpoint_nrz_nib_legacy' : 11824.122,
        't4_midpoint_pam4_nib_legacy' : 11824.122,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_50g_23():
    return {
        'linerate' : '50GLanes2',              
        'interface'  :'QSFP28',
        'fec_status' : 'false',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 11481.496,
        't4_midpoint_nrz_nib' : 11481.496,
        't4_midpoint_pam4_nib' : 11481.496,
        't4_midpoint_nrz_jib_legacy' : 11481.496,
        't4_midpoint_nrz_nib_legacy' : 11481.496,
        't4_midpoint_pam4_nib_legacy' : 11481.496,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_50g_23_fec():
    return {
        'linerate' : '50GLanes2',              
        'interface'  :'QSFP28',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_nrz_jib' : 11824.126,
        't4_midpoint_nrz_nib' : 11824.126,
        't4_midpoint_pam4_nib' : 11824.126,
        't4_midpoint_nrz_jib_legacy' : 11824.126,
        't4_midpoint_nrz_nib_legacy' : 11824.126,
        't4_midpoint_pam4_nib_legacy' : 11824.126,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }
#f for Finisar
def sfp56_f_fec():
    return {
        'linerate' : '50G',
        'interface'  :'SFP56F',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 11475.191,
        't4_midpoint_pam4_nib_legacy' : 11475.191,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Finisar
def sfp56_f_fec_flexe():
    return {
        'linerate' : '50G',
        'interface'  :'SFP56F',
        'fec_status' : 'true',
        'flexe_status' : '_FlxE',
        't4_midpoint_pam4_nib' : 159.605,
        't4_midpoint_pam4_nib_legacy' : 159.605,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Gigalight
def sfp56_g_fec():
    return {
        'linerate' : '50G',
        'interface'  :'SFP56G',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 11509.189,
        't4_midpoint_pam4_nib_legacy' : 11509.189,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Gigalight
def sfp56_g_fec_flexe():
    return {
        'linerate' : '50G',
        'interface'  :'SFP56G',
        'fec_status' : 'true',
        'flexe_status' : '_FlxE',
        't4_midpoint_pam4_nib' : 147.973,
        't4_midpoint_pam4_nib_legacy' : 147.973,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }

def qsfp28_100g():
    return {
        'linerate' : '100G',              
        'interface'  :'QSFP28',
        'fec_status' : 'false',
        'flexe_status' : '',
        'full_interface_name' : 'QSFP28_100G',
        't4_midpoint_nrz_jib' : 6973.194,
        't4_midpoint_nrz_nib' : 6973.194,
        't4_midpoint_pam4' : 6973.194,
        't4_midpoint_nrz_jib_legacy' : 6973.194,
        't4_midpoint_nrz_nib_legacy' : 6973.194,
        't4_midpoint_pam4_nib_legacy' : 7311.389,
        'tolerance' : 5,

        'fec_possible' : True,
        'flexe_possible' : True,
        'fec_enabled' : False,
        'flexe_enabled' : False,
        'default_linerate' : False,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_100g_fec():
    return {
        'linerate' : '100G',              
        'interface'  :'QSFP28',
        'fec_status' : 'true',
        'flexe_status' : '',
        'tolerance' : 5,
        'full_interface_name' : 'Qsfp28_100G_fec',
        't4_midpoint_nrz_jib' : 9999999,
        't4_midpoint_nrz_nib' : 7047.762,
        't4_midpoint_pam4' : 7047.762,
        'tolerance' : 5,
        'fec_possible' : True,
        'flexe_possible' : True,
        'default_linerate' : False,

        'fec_enabled'  :True,
        'flexe_enabled'  :False,


        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_100g_flexe():
    return {
        'linerate' : '100G',
        'interface'  :'QSFP28',
        'fec_status' : 'false',
        'flexe_status' : '_FlxE',
        't4_midpoint_nrz_jib' : 278.706,
        't4_midpoint_nrz_nib' : 278.706,
        't4_midpoint_pam4_nib' : 278.706,
        't4_midpoint_nrz_jib_legacy' : 278.706,
        't4_midpoint_nrz_nib_legacy' : 278.706,
        't4_midpoint_pam4_nib_legacy' : 278.706,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def qsfp28_100g_fec_flexe():
    return {
        'linerate' : '100G',
        'interface'  :'QSFP28',
        'fec_status' : 'true',
        'flexe_status' : '_FlxE',
        't4_midpoint_nrz_jib' : 358.169,
        't4_midpoint_nrz_nib' : 358.169,
        't4_midpoint_pam4_nib' : 358.169,
        't4_midpoint_nrz_jib_legacy' : 358.169,
        't4_midpoint_nrz_nib_legacy' : 358.169,
        't4_midpoint_pam4_nib_legacy' : 358.169,
        'tolerance' : 1.5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }

def cxp():
    return {
        'linerate' : '100G',
        'interface'  :'CXP',
        'fec_status' : 'false',
        'flexe_status' : '',
        'full_interface_name' : 'Cxp',
        't4_midpoint_nrz_jib' : 6976.201,
        't4_midpoint_nrz_legacy' : 6976.201,
        'tolerance' : 1.5,
        'fec_possible' : False,
        'flexe_possible' : False,
        
        'default_linerate' : True,
        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 1.5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 1.5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 1.5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 1.5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 3,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 1.5

    }
#Finisar FR4 optics
def qsfpdd_ffr4_fec():
    return {
        'linerate' : '400G',
        'interface'  :'QSFPDDFFR4',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 5317.459,
        't4_midpoint_pam4_nib_legacy' : 5317.459,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Finisar FR8 optics
def qsfpdd_ffr8_fec():
    return {
        'linerate' : '400G',
        'interface'  :'QSFPDDFFR8',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 5312.959,
        't4_midpoint_pam4_nib_legacy' : 5312.959,
        'tolerance' : 5,


        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Finisar LR8 optics
def qsfpdd_flr8_fec():
    return {
        'linerate' : '400G',
        'interface'  :'QSFPDDFLR8',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 5312.959,
        't4_midpoint_pam4_nib_legacy' : 5312.959,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
#Finisar SR8 optics
def qsfpdd_fsr8_fec():
    return {
        'linerate' : '400G',
        'interface'  :'QSFPDDFSR8',
        'fec_status' : 'true',
        'flexe_status' : '',
        't4_midpoint_pam4_nib' : 5314.959,
        't4_midpoint_pam4_nib_legacy' : 5314.959,
        'tolerance' : 5,

        'onepps' : 0,
        'onepps_tolerance' : 1,
        'onepps_cte' : 0,
        'onepps_cte_tolernace' : 0.99,

        'two_way' : 0,
        'two_way_tolerance' : 5,

        'fwd_cf_Accuracy' : 50,
        'fwd_cf_accuracy_tolerance' : 5,
        'fwd_latency' : 50,
        'fwd_latency_tolerance' : 5,
        'fwd_cf_delta' : 0,
        'fwd_cd_delta_tolerance' : 5,

        'pdel_fwd_cf_accuracy' : 100,
        'pdel_fwd_cf_accuracy_tolerance' : 10,        # this probably wont be needed as it is just 2xnormal tolerance

        'cte_tolerance' : 0.8, 
        'two_way_cte' : 0,
        't1_cte_dte' : 'na', # this is t4 midpoint * -1
        't4_cte_dte' : 't4 midpoint', # t4 midpoint
        'two_way_cte_dte' : 0,
        '1pps_cte_dte' : 0,

        'rte' : 0,
        'rte_tolerance' : 5

    }
