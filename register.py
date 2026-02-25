from tkinter import *
import tkinter as tk
import mysql.connector
from datetime import date
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import Message
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Hotel_management"
)
cur=db.cursor()
#print(db)
#print(date.today())
root=tk.Tk()
root.geometry("600x400")
root.title("Welcome to owner registration")
frm=tk.Frame(root).grid(padx=20,pady=20)

tk.Label(frm,text="OWNER REGISTRATION",anchor=tk.CENTER,wraplength=300,fg="red").grid(row=0,column=2)
tk.Label(frm,text="(all fields are mandatory to fill)").grid(row=1,column=1)
tk.Label(frm,text="Aadhar").grid(row=2,column=0)
ad=tk.Entry(frm)
ad.grid(row=2,column=1)
tk.Label(frm,text="First name").grid(row=3,column=0)
fn=tk.Entry(frm)
fn.grid(row=3,column=1)
tk.Label(frm,text="Last name").grid(row=4,column=0)
ln=tk.Entry(frm)
ln.grid(row=4,column=1)
tk.Label(frm,text="D.O.B.").grid(row=5,column=0)
#tk.Entry(frm).grid(row=5,column=1)
dob=DateEntry(root,width=17,background='darkblue', foreground='white', borderwidth=2,date_pattern="yyyy-mm-dd")
dob.grid(row=5, column=1)
tk.Label(frm,text="Contact no.").grid(row=6,column=0)
cno=tk.Entry(frm)
cno.grid(row=6,column=1)
tk.Label(frm,text="Password").grid(row=7,column=0)
ps=tk.Entry(frm)
ps.grid(row=7,column=1)
tk.Label(frm,text="Confirm Password").grid(row=8,column=0)
cps=tk.Entry(frm)
cps.grid(row=8,column=1)
owner={}
def owner_det():
    owner.clear()
    sql="SELECT * FROM owner"
    cur.execute(sql)
    result=cur.fetchall()
    for o in result:
        owner[o[3]]={"id":o[1],"password":o[4],"name":o[5],"dob":o[6],"contact_no":o[7],"state":o[8]}
owner_det()
#print(owner) 
def register():
    aadhar=ad.get()
    f_nm=fn.get()
    l_nm=ln.get()
    #d_o_b=dob.get()
    d_o_b = datetime.strptime(dob.get(), "%Y-%m-%d").date()
    c_no=cno.get()
    pas=ps.get()
    cpas=cps.get()
    if aadhar == "":
        msg=Message(frm,text="Enter aadhar",fg="red",width="250")
        msg.grid(row=12,column=1)
    elif aadhar in owner:
        #print("yes")
        msg=Message(frm,text="Already register with this aadhar number",fg="red",width="250")
        msg.grid(row=12,column=1)
    elif f_nm == "":
        msg=Message(frm,text="Enter name",fg="red",width="250")
        msg.grid(row=12,column=1)
    elif l_nm == "":
        msg=Message(frm,text="Enter name", fg="red", width="250")
        msg.grid(row=12,column=1)
    elif d_o_b == date.today():
        msg=Message(frm,text="Enter DOB", fg="red", width="250")
        msg.grid(row=12,column=1)
    elif c_no== "":
        msg=Message(frm,text="Enter Contact",fg="red",width="250")
        msg.grid(row=12,column=1)
    elif pas=="":
        msg=Message(frm,text="Enter Password",fg="red",width="250")
        msg.grid(row=12,column=1)
    elif cpas=="":
        msg=Message(frm,text="Confirm Password",fg="red",width="250")
        msg.grid(row=12,column=1)
#register()        
tk.Button(frm,text="Submit",command=register,bg="green",fg="white",width=10).grid(row=11,column=0)
tk.Button(frm,text="Reset",command=root.destroy,bg="red",fg="white",width=10).grid(row=11,column=1)

root.mainloop()