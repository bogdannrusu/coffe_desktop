import sys
import mysql.connector


def connect():
    conn = None
    try:
        conn = mysql.connector.Connect(
            host="localhost",
            username="root",
            password="Ban4ever!#",
            database="coffee_le_coupage",
            port="3305"
        )

        print( "Connected" )

    except:
        print( "Error", sys.exc_info() )

    finally:
        return conn


connect()
