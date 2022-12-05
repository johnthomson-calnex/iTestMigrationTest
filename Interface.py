#############################################################
#                                                           #
#   This class takes in the interface dictionary and        #
#   constructs an interface from it that will contain all   #
#   the relevant limits                                     #    
#                                                           #
#############################################################
import csv

class Interface():

    def __init__(self, interface_dict, hardware_type):
        """
        The function takes in a dictionary of values and a hardware type. It then uses the values in the
        dictionary to set the values of the class
        
        :param interface_dict: This is a dictionary of the interface parameters
        :param hardware_type: This is the type of hardware that the interface is on. This is used to
        determine the T4 midpoint
        """
        self.interface_dict = interface_dict
        self.linerate = interface_dict['linerate']
        self.t4_midpoint = interface_dict[f"t4_midpoint_{hardware_type}"]
        self.tolerance = interface_dict['tolerance']
        self.interface_name = f"{interface_dict['linerate']}_{interface_dict['interface']}_{interface_dict['fec_status']}{interface_dict['flexe_status']}_HA"
        self.full_interface_name = interface_dict['full_interface_name']
        self.interface_type = interface_dict['interface']
        self.default_linerate = interface_dict['default_linerate']
        self.has_fec = interface_dict['has_fec']
        self.has_flexe = interface_dict['has_flexe']

        self.t4_max = self.t4_midpoint + self.tolerance
        self.t4_min = self.t4_midpoint - self.tolerance

        self.t1_midpoint = self.t4_midpoint * -1
        self.t1_min = self.t1_midpoint - self.tolerance
        self.t1_max = self.t1_midpoint + self.tolerance

        self.fwd_cf_accuracy_midpoint = 50
        self.fwd_cf_accuracy_min = self.fwd_cf_accuracy_midpoint - self.tolerance
        self.fwd_cf_accuracy_max = self.fwd_cf_accuracy_midpoint + self.tolerance

        self.fwd_cf_delta_midpoint = 0
        self.fwd_cf_delta_min = self.fwd_cf_delta_midpoint - self.tolerance
        self.fwd_cf_delta_max = self.fwd_cf_delta_midpoint + self.tolerance

        self.fwd_latency_midpoint = 50
        self.fwd_latency_min = self.fwd_latency_midpoint - self.tolerance
        self.fwd_latency_max = self.fwd_latency_midpoint + self.tolerance

        self.bc_fwd_latency_midpoint = -50
        self.bc_fwd_latency_min = self.bc_fwd_latency_midpoint - self.tolerance
        self.bc_fwd_latency_max = self.bc_fwd_latency_midpoint + self.tolerance

        self.pdel_fwd_cf_accuracy_midpoint = 100        
        self.pdel_tolerance = 2 * self.tolerance
        self.pdel_fwd_cf_accuracy_min = self.pdel_fwd_cf_accuracy_midpoint - self.pdel_tolerance
        self.pdel_fwd_cf_accuracy_max = self.pdel_fwd_cf_accuracy_midpoint + self.pdel_tolerance

        self.onepps_max = 1
        self.onepps_min = -1

        self.isLegacy = False
        self.is_mixed_rates = False
        self.hardware_type = hardware_type

        self.mom_movement = 1.0
        self.pdel_mom_movement = 1.5

        self.t1_data_points = []
        self.t4_data_points = []
        self.twoway_data_points = []
        self.onepps_data_points = []
        self.fwd_latency_data_points = []
        self.fwd_cf_delta_data_points = []
        self.fwd_cf_accuracy_data_points = []
        self.pdel_fwd_cf_accuracy_data_points = []
        self.data = []

        self.sub1_data = []
        self.sub2_data = []
        self.t1_data_points_sub1 = []
        self.t4_data_points_sub1 = []
        self.twoway_data_points_sub1 = []
        self.t1_data_points_sub2 = []
        self.t4_data_points_sub2 = []
        self.twoway_data_points_sub2 = []

        self.t1_cte_data_points =[]
        self.t4_cte_data_points = []
        self.t1_cte_dte_data_points = []
        self.t4_cte_dte_data_points = []
        self.two_way_cte_data_points = []
        self.two_way_cte_dte_data_points = []

        self.cte_tolerance = interface_dict["cte_tolerance"]
        self.t1_cte_min = self.t1_midpoint - self.cte_tolerance
        self.t1_cte_max = self.t1_midpoint + self.cte_tolerance
        self.t4_cte_min = self.t4_midpoint - self.cte_tolerance
        self.t4_cte_max = self.t4_midpoint + self.cte_tolerance
        self.two_way_cte_min = 0 - self.cte_tolerance
        self.two_way_cte_max = 0 + self.cte_tolerance

        self.t4_mean_of_means = 0

        self.largest_t1_breach = 0
        self.largest_t4_breach = 0
        self.largest_2way_breach = 0

        #Mean of means ref. Other metrics are just the midpoints ie T1,T4, Latency etc
        self.onepps_ref_mom = 0
        self.tc_ref_mom = 0
        self.twoway_ref_mom = 0


    #
    #   The following methods are used to add specific data points to the interface.
    #   add data rows functions take in an entire row of the csv file and add it to a list.
    #   add data point functions take in a list of 3 elements containing [min,mean,max] values and add it to a data points list, this data points list is a list of lists.  
    #

    def add_t4_mean_of_means(self,val):
        self.t4_mean_of_means = val
        
    def add_data_row(self,row):        
        self.data.append(row)

    def add_sub1_data_row (self,row):
        self.sub1_data.append(row)

    def add_sub2_data_row(self,row):
        self.sub2_data.append(row)

    def add_sub_t1_data_point(self,t1_data_point_list,sub):
        if sub == "sub1":
            self.t1_data_points_sub1.append(t1_data_point_list)
        else:   
            self.t1_data_points_sub2.append(t1_data_point_list)
    
    def add_sub_t4_data_point(self,t4_data_point_list,sub):
        if sub == "sub1":
            self.t4_data_points_sub1.append(t4_data_point_list)
        else:   
            self.t4_data_points_sub2.append(t4_data_point_list)

    def add_sub_2way_data_point(self,twoway_data_point_list,sub):
        if sub == "sub1":
            self.twoway_data_points_sub1.append(twoway_data_point_list)
            
        else:   
            self.twoway_data_points_sub2.append(twoway_data_point_list)

    def add_t1_data_point(self,t1_data_point_list):
        self.t1_data_points.append(t1_data_point_list)

    def add_t4_data_point(self,t4_data_point_list):
        self.t4_data_points.append(t4_data_point_list)

    def add_2way_data_point(self,twoway_data_point_list):
        self.twoway_data_points.append(twoway_data_point_list)

    def add_t1_data_point_rte(self,t1_data_point_list,sub):
        self.t1_data_points_sub1.append(t1_data_point_list) if sub == "sub1" else self.t1_data_points_sub2.append(t1_data_point_list)        

    def add_t4_data_point_rte(self,t4_data_point_list,sub):
        self.t4_data_points_sub1.append(t4_data_point_list) if sub == "sub1" else self.t4_data_points_sub2.append(t4_data_point_list)

    def add_2way_data_point_rte(self,twoway_data_point_list,sub):
        self.twoway_data_points_sub1.append(twoway_data_point_list) if sub == "sub1" else self.twoway_data_points_sub2.append(twoway_data_point_list)        

    def add_1pps_data_point(self,onepps_data_point_list):
        self.onepps_data_points.append(onepps_data_point_list)

    def add_fwd_latency_data_point(self,fwd_latency_data_points_list):
        self.fwd_latency_data_points.append(fwd_latency_data_points_list)
    
    def add_fwd_cf_Delta_data_point(self,fwd_cf_delta_data_points_list):
        self.fwd_cf_delta_data_points.append(fwd_cf_delta_data_points_list)
    
    def add_fwd_cf_Accuracy_data_point(self,fwd_cf_accuracy_data_points_list):
        self.fwd_cf_accuracy_data_points.append(fwd_cf_accuracy_data_points_list)

    def add_pdel_fwd_cf_Accuracy_data_point(self,pdel_fwd_cf_accuracy_data_points_list):
        self.pdel_fwd_cf_accuracy_data_points.append(pdel_fwd_cf_accuracy_data_points_list)

    def add_t1_cte_data_point(self,points_list, type):
        self.t1_cte_data_points.append(points_list) if type=="cte" else self.t1_cte_dte_data_points.append(points_list)
    
    def add_t4_cte_data_point(self,points_list,type):
        self.t4_cte_data_points.append(points_list) if type == "cte" else self.t4_cte_dte_data_points.append(points_list)

    def add_2way_cte_data_point(self,points_list,type):
        self.two_way_cte_data_points.append(points_list) if type == "cte" else self.two_way_cte_dte_data_points.append(points_list)

    

    def set_legacy_timestamping(self):
        """
        This function sets the timestamping to legacy mode, and so sets the legacy limits
        """
        self.isLegacy = True
        self.t4_midpoint = self.interface_dict[f"t4_midpoint_{self.hardware_type}_legacy"]
        self.t4_max = self.t4_midpoint + self.tolerance
        self.t4_min = self.t4_midpoint - self.tolerance

        self.t1_midpoint = self.t4_midpoint * -1
        self.t1_min = self.t1_midpoint - self.tolerance
        self.t1_max = self.t1_midpoint + self.tolerance

    def set_mixed_rates(self):
        """
        This function sets mixed_rates to True and calculates the new limits with an additional 250ps of noise allowance
        """
        self.is_mixed_rates = True
        self.tolerance += 0.25
        self.t4_max = self.t4_midpoint + self.tolerance
        self.t4_min = self.t4_midpoint - self.tolerance
        
        self.t1_min = self.t1_midpoint - self.tolerance
        self.t1_max = self.t1_midpoint + self.tolerance

    #
    #   The following functions are used to get specific data from the interface
    #

    def get_all_t1_data_points(self):
        return self.t1_data_points

    def get_all_t4_data_points(self):
        return self.t4_data_points

    def get_all_2way_data_points(self):
        return self.twoway_data_points

    def get_all_t1_data_points_rte(self,sub):
       return self.t1_data_points_sub1 if sub == "sub1" else self.t1_data_points_sub2
       
    
    def get_all_t4_data_points_rte(self,sub):
        return self.t4_data_points_sub1 if sub == "sub1" else self.t4_data_points_sub2

    def get_all_2way_data_points_rte(self,sub):
        return self.twoway_data_points_sub1 if sub == "sub1" else self.twoway_data_points_sub2

    def get_all_1pps_data_points(self):
        return self.onepps_data_points

    def get_all_fwd_latency_data_points(self):
        return self.fwd_latency_data_points
    
    def get_all_fwd_cf_accuracy_data_points(self):
        return self.fwd_cf_accuracy_data_points

    def get_all_fwd_cf_Delta_data_points(self):
        return self.fwd_cf_delta_data_points

    def get_all_pdel_fwd_cf_accuracy_data_points(self):
        return self.pdel_fwd_cf_accuracy_data_points
    
    def has_data(self):
        return len(self.data) > 0 or len(self.sub1_data) > 0 or len(self.sub2_data) > 0

    def get_data(self, sub=None):
        if not sub:
            return self.data
        else:
            return self.sub1_data if sub == "sub1" else self.sub2_data


    def get_sub1_data(self):
        return self.sub1_data

    def get_sub2_data(self):
        return self.sub2_data

    def get_all_t1_cte_data_points(self,type):
        return self.t1_cte_data_points if type=="cte" else self.t1_cte_dte_data_points

    def get_all_t4_cte_data_points(self,type):
        return self.t4_cte_data_points if type == "cte" else self.t4_cte_dte_data_points

    def get_all_2way_cte_data_points(self,type):
        return self.two_way_cte_data_points if type == "cte" else self.two_way_cte_dte_data_points

    @staticmethod        
    def get_means_from_data_points(data_point_list):
        """
        It takes a list of data points (which is list of points [min,mean,max]) and returns a list of the mean
        values
        
        :param data_point_list: a list of data points
        :return: The means of the data points.
        """
        return [point[1] for point in data_point_list]

    def create_csv(self, test_mode):   
        """
        It creates a csv file with the data from the self.data variable
        
        :param test_mode: "rte" or any other
        """
        if test_mode == "rte":
            self.create_rte_csv()
        else:
            with open(f"Results/{self.interface_name}/CSV/{self.interface_name}_{test_mode}.csv", 'w', newline='') as file:        
                fieldnames = self.data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for row in self.data:
                    writer.writerow(row)
                 

    def create_rte_csv(self):
        """
        It creates two csv files, one for each of the two subs, and writes the data to the csv
        files.
        """
        with open(f"Results/{self.interface_name}/CSV/{self.interface_name}_rTE_sub1.csv", 'w', newline='') as file: 
            fieldnames = self.sub1_data[0].keys()
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for row in self.sub1_data:
                writer.writerow(row)
        
        with open(f"Results/{self.interface_name}/CSV/{self.interface_name}_rTE_sub2.csv", 'w', newline='') as file: 
            fieldnames = self.sub2_data[0].keys()
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for row in self.sub2_data:
                writer.writerow(row)

    
    def on_limit_breach(self,limit_type,value):
        if limit_type == "t1":
            if value > self.largest_t1_breach: self.largest_t1_breach = value
        if limit_type == "t4":
            if value > self.largest_t4_breach: self.largest_t4_breach = value
        if limit_type == "2way":
            if value > self.largest_t1_breach: self.largest_2way_breach = value