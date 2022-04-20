import sqlite3
import time
import math
from traceback import print_tb
from datetime import datetime

#SETTINGS
store_Interval = 60 * 60

# Connecting to sqlite
 
def CreateTable(currentTime, cursor_obj, connection_obj):
    # Creating table
    tbl = """
                CREATE TABLE t""" + str(currentTime) + """(
                Plane_In_Air INT,
                Emission_Ton INT,
                Time INT
        )"""
    cursor_obj.execute(tbl);
    connection_obj.commit()
    print(cursor_obj)
    # Close the connection
    cursor_obj.close()
def StoreTimeStamp(emision, planeinair):
    currentTime = int(time.time())
    currentHourStamp = math.floor(currentTime / store_Interval)
    now = datetime.now()
    Current_Min = now.strftime("%M")
    connection_obj = sqlite3.connect('/Users/johannes/Git-Prosjekter/Miljø_Prosjekt/Store/database.db')
    cursor_obj = connection_obj.cursor()
    # Check table stamp exist
    try:
        cursor_obj.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("t" + str(currentHourStamp),))
        ret = bool(cursor_obj.fetchone())
        if not ret:
            print("Create new table")
            CreateTable(currentHourStamp, cursor_obj, connection_obj)
            connection_obj.commit()
        cursor_obj = connection_obj.cursor()
        GetDataQuery =  "INSERT INTO {} VALUES({}, {}, '{}')".format("t" + str(currentHourStamp), planeinair, emision, Current_Min)
        cursor_obj.execute(GetDataQuery);
        connection_obj.commit()
        return ret
    except:
        print("Error")
    # Close the connection
    connection_obj.close()