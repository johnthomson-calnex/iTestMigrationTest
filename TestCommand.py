from Command import Command, GET,PUT,Session


neo = Session("100g-vm9")
profile = neo.get_response("/api/app/mse/ptpprofile")
print(profile["PtpProfile"])


p = neo.get_value("/api/app/mse/ptpprofile", "PtpProfiles")
print(p)

# print(profile["PtpProfile"])

# neo.put("/api/app/mse/ptpprofile?PtpProfile=Profile_CCSA")

# new_profile ,cmd = neo.get_with_cmd("/api/app/mse/ptpprofile")

# print(new_profile["PtpProfile"])
# print(cmd.start)


# for cmd in neo.get_all_commands():
#     print(cmd)