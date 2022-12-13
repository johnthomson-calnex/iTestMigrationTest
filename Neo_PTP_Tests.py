from Command import Session
from Interface import Interface
import Paragon_Procedure_Library
import time

def ptp_test(session : Session, interface : Interface, encapsulation : str = "Ethernet") -> bool:

    test_result = True

    #Check if the interface is flexe and non ethernet then return
    if interface.flexe_possible and interface.flexe_enabled and not encapsulation == "Ethernet":
        #TODO call a 'check FlexE is disabled in the app' method
        Paragon_Procedure_Library.print_information(f"{interface.full_interface_name} has FlexE enabled and as it is not Ethernet encapsulation, this test cannot run.")
        return True

    #set up clock ref
    Paragon_Procedure_Library.set_clock_reference(session)

    #set ptp profile
    Paragon_Procedure_Library.set_ptp_profile(session, "Profile_G_8275_1")

    #set up link
    if not Paragon_Procedure_Library.setup_interface(session, interface) and not Paragon_Procedure_Library.check_link(session,interface):
        Paragon_Procedure_Library.print_fail(f"Failed to set up link for {interface}")
        return False
    else:
        Paragon_Procedure_Library.print_pass(f"Successfully set up {interface.full_interface_name}")
        session.put("/api/app/mse/measurement/start")
        time.sleep(10)
        session.put("/api/app/mse/measurement/stop")
        session.put("/api/app/mse/master/master1/stop")

        # Check CAT
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "Sync", "D", "TIMEERROR", "-", "Min"):
            test_result = False
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "Sync", "D", "TIMEERROR", "-", "Max"):
            test_result = False
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "Sync", "D", "TIMEERROR", "-", "Mean"):
            test_result = False
        
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "DelayReq", "D", "TIMEERROR", "-", "Min"):
            test_result = False
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "DelayReq", "D", "TIMEERROR", "-", "Max"):
            test_result = False
        if not Paragon_Procedure_Library.check_cat_result_for_metric(session,interface,"end_to_end", "DelayReq", "D", "TIMEERROR", "-", "Mean"):
            test_result = False
    
    return test_result