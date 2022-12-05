import schedule
import time,sys,os

_TESTING = True
_parameter_file = "Param1.py"

tests_to_run = ["TestCase1.py", "TestCase2.pyd", "PTP/PTP_Test_1.py"]



def verify_tests_exist():
    tests_failed_to_find = []
    for test in tests_to_run:
        if not os.path.exists(test):
            tests_failed_to_find.append(test)

    if  len(tests_failed_to_find) > 0:
        print(f"Failed to find the following tests {tests_failed_to_find}. Script will now wait 20s to give you a chance to kill it and correct the mistake or run without testing them.")
        time.sleep(20)


def job():
    global _TESTING
    for test in tests_to_run:    
        if os.path.exists(test):        
            os.system(f"python {test} {_parameter_file} ")
            print("\n")
    _TESTING = False


verify_tests_exist()




schedule.every().hour.at(":08").do(job)

while _TESTING:
    schedule.run_pending()
    time.sleep(1)
   