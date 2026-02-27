import mysql.connector
import tkinter as tk
from tkinter import Message
import time
from datetime import date
db=mysql.connector.connect(
		host="Localhost",
		user="root",
		password="",
		database="hotel_management",
		#port=""
)
cur=db.cursor()
def start(owner,username):
    t=time.strftime("%H:%M:%S")
    d=date.today()
    #print(d,t)
    #print(db)
    root=tk.Tk()
    root.geometry("600x600")
    frm=tk.Frame(root,width="500",height="500")
    frm.grid(row=2,column=2)
    tk.Label(frm,text="Welcome to register your hotel",bg="red",fg="white",width="30",font=("Arial",16,"bold")).grid(row=2,column=2)
    tk.Label(frm,text="Enter Hotel name :").grid(row=3,column=0)
    hn=tk.Entry(frm,width="50")
    hn.grid(row=3,column=1)
    def hnm():
        hn1=hn.get()
        if hn1 == "":
            msg=Message(frm,text="Enter hotel name",fg="red",width="250")
            msg.grid(row=5,column=1)
        else:
            #print("Hotel added successfully")
            sql="Insert into `hotels` (`date`,`time`,`owner_id`,`hotel_name`,`status`,`state`) VALUES (%s,%s,%s,%s,%s,%s)"
            val=(d,t,owner[username]["id"],hn1,"open","active")
            cur.execute(sql,val)
            db.commit()
            msg=Message(frm,text="Hotel added Successfully",fg="green",width="250")
            msg.grid(row=5,column=1)
            hn.delete(0,tk.END)
            #time.sleep(5)
            #root.destroy()
    tk.Button(frm,text="Save",command=hnm,bg="green",fg="white",activebackground="sky blue",width="10").grid(row=4,column=0)
    tk.Button(frm,text="Cancel",command=root.destroy,bg="red",fg="white",activebackground="blue",width="10").grid(row=4,column=1)
    root.mainloop()