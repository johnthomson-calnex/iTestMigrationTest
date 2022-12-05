from Command import Command, GET,PUT,Session


neo = Session("100g-vm2")
profile = neo.get("/api/app/mse/ptpprofile")

print(profile["PtpProfile"])

neo.put("/api/app/mse/ptpprofile?PtpProfile=Profile_CCSA")

new_profile ,cmd = neo.get_with_cmd("/api/app/mse/ptpprofile")

print(new_profile["PtpProfile"])
print(cmd.start)


for cmd in neo.get_all_commands():
    print(cmd)