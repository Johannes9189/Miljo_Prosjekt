import time
from itsdangerous import exc


while True:
    try:
        print("Server started")
    except:
        print("Error")
    time.sleep(1)