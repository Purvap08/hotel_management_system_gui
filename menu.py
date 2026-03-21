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
def menu_cat(selected_id,owner,username):  
    sql="SELECT * from `menu_category` WHERE `owner_id`= %s AND `hotel_id` = %s"
    val=(owner[username]["id"],selected_id)
    cur.execute(sql,val)
    result=cur.fetchall()
    #print(result)
    menu_c.clear()
    for m in result:
        menu_c.append({"id":m[0],"name":m[5]})
        mcat.append(m[0])
        mcatnm.append(m[5])
m_nm={}        
def menu_l(selected_id,owner,username):
    sql="SELECT * FROM `menu` WHERE `owner_id` = %s AND `hotel_id` = %s"
    val=(owner[username]["id"],selected_id)
    cur.execute(sql,val)
    result=cur.fetchall()
    for m in result:
        m_nm[m[0]]={"category_id":m[5],"hotel_id":m[4],"name":m[6],"price":m[7],"status":m[8]}
    #print(m_nm)    
def check(selected_id,owner,username):
    menu_cat(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Check Menu Category")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=1,column=1)
    frm.pack(padx=10,pady=10)
    #print(menu_c)
    tk.Label(frm,text="Check Category",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).pack(padx=10,pady=10)
    table=ttk.Treeview(root)
    table['columns']=('Id','Name')
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Id', anchor=tk.W, width=150)
    table.column('Name', anchor=tk.W, width=200)
    table.heading('#0', text='', anchor=tk.W)
    table.heading('Id', text='Id', anchor=tk.W)
    table.heading('Name', text='Name', anchor=tk.W)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)    