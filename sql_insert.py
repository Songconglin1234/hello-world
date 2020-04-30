import pandas as pd
import pymysql
import requests
import io
import csv 

def connect_db(db_name):
    conn = pymysql.connect(host = 'localhost', user = 'root',password = 'test',db = db_name)
    cursor1  = conn.cursor()
    return conn, cursor1

def insert_data(db_name, table_name):
    conn,mycursor = connect_db(db_name)

    f = open("C:\\Users\\16262\\hello-world\\companylist.csv")
    readerlist = csv.reader(f)

   # pdata = pd.read_csv()

    for ori ,des, dur in readerlist:
       mycursor.execute(" INSERT INTO flights (origin, destination, duration) VALUE (%s,%s,%s)", (ori, des,dur ))
       print("insert into database values {origin, destination, duration}", ori, des, dur )

    print(str(conn) + str(mycursor)) 
    conn.commit()
 #   f.close()

    h_files = open("C:\\Users\\16262\\hello-world\\passenger.csv")
    readerlist1 = csv.reader(h_files)

    for id, passa ,flis in readerlist1:
       mycursor.execute(" INSERT INTO passengers ( name, flight_id) VALUE (%s,%s)", (passa, flis ))
       print("insert into table passagers values {passager_name, flights_id}", passa, flis )

    h_files.close()
    conn.commit()
    conn.close()
    mycursor.close()

insert_data('flights','flights')
 


   

