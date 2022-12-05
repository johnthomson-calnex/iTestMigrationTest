import sys,os

try:
    test = sys.argv[1]
    param = sys.argv[2]

    res = os.system(f"Python {test} {param}")
    print(res)

except Exception as e:
    print(e)