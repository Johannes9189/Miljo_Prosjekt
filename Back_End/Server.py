from multiprocessing.connection import wait
import time
import random
from storehandler import *
from itsdangerous import exc

updatestamp = 60 * 0.1

def Getaerostat():
    return random.randint(7500, 20000), random.randint(13000, 17408)
def UpdateStamp():
    print("Fetching current flight data")
    Plane_In_Air, Carbon_In_Air = Getaerostat()
    StoreTimeStamp(Carbon_In_Air,Plane_In_Air)
print("Server started")
while True:
    try:
        UpdateStamp()
    except:
        print("Fetch failed")
    time.sleep(updatestamp)