import sqlite3
import time
import math

#SETTINGS
store_Interval = 60 * 60

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('/Users/johannes/Git-Prosjekter/Miljø_Prosjekt/Store/database.db')
 
def CreateTable(currentTime, cursor_obj):
    # Creating table
    table = """ CREATE TABLE """ + str(currentTime) + """ + (
                Plane_In_Air INT,
                Emission_Ton INT,
            ); """
    # Close the connection
    cursor_obj.close()
def StoreTimeStamp(emision, planeinair):
    currentTime = int(time.time())
    currentHourStamp = math.floor(currentTime / store_Interval)
    cursor_obj = connection_obj.cursor()
    # Check table stamp exist
    try:
        cursor_obj.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name=?;
        """, (str(currentHourStamp),))
        ret = bool(cursor_obj.fetchone())
        if ret:
            print("Table already exist",)
        else:
            print("Create new table")
            CreateTable(currentHourStamp, cursor_obj)
        return ret
    except:
        print("Error")
    # Close the connection
    connection_obj.close()
StoreTimeStamp(21,3)