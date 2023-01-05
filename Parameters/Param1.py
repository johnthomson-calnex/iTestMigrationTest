
class Global_Parameters:

    def __init__(self):
        self.param_name = "Parameter File 1"
        self.unit_name = "Virtual"
        self.hardware_type = "pam4"
        self.unit_ip = "100g-vm6"
        self.rj45_cable_comp = 5.678
        self.ptp_te_check = True,
        self.g_mask = "defaults"
        self.clock_reference = "internal"
        self.run_id = {
            "independant" : 0,
            "Qsfp28_100G_fec" : 12,
            "Qsfp28_100G" : 2,
            "Sfp1G" : 3,
            "Cxp" : 4,
            "Sfp28" : 5,
            "Sfp28_fec" : 6
        }
        self.cable_compensation = {
            "QSFP28" : 5.456,
            "CXP" : 5.403,
            "SFP1G" : 0.567
        }



