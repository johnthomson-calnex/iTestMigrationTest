import importlib,sys

def get_interfaces():
    module = importlib.import_module(f"Parameters.Interfaces_Mask")   
    p = sys.argv[2]
    f = p.replace("/",".").replace(".py", "")
    param_file = importlib.import_module(f"{f}")
    gp = param_file.Global_Parameters()
    mask = gp.g_mask
    mask_func = getattr(module,mask)
    all_interfaces_in_mask = mask_func()
    interfaces_to_test = [i for i in all_interfaces_in_mask if all_interfaces_in_mask[i]]

    return interfaces_to_test