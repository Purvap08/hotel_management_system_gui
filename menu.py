import mysql.connector
import time
from datetime import date
import tkinter as tk
from tkinter import *
from tkinter import ttk
import select_hotels
import logout1
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel_management",
    #port=""
)
cur=db.cursor()
#print(db)
d=date.today()
t=time.strftime("%H:%M:%S")
#print(d,t)
m_nm={}
def menu(selected_id,owner,username):
    sql="SELECT * FROM `menu` WHERE `owner_id` = %s AND `hotel_id` = %s"
    val=(owner[username]["id"],selected_id)
    cur.execute(sql,val)
    result=cur.fetchall()
    for m in result:
        m_nm[m[4]]={"category_id":m[5],"id":m[0],"name":m[6],"price":m[7],"status":m[8]}
    print(m_nm)    