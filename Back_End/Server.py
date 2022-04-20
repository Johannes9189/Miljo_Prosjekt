from multiprocessing.connection import wait
import time
from storehandler import *
from itsdangerous import exc

updatestamp = 60 * 10

def UpdateStamp():
    print("Fetching current flight data")
    StoreTimeStamp(21,3)
while True:
    try:
        print("Server started")
        UpdateStamp()
    except:
        print("Fetch failed")
    time.sleep(updatestamp)