import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector  
from datetime import date
from tkinter import Message
import time
import re
import register
import buttons
import add_hotel
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel_management"
)
cur=db.cursor()
d=date.today()
t=time.strftime("%H:%M:%S")
#print(d,t)
#print(db)
def log_in(): 
    owner={}
    def choose_hotel(username):
        root.destroy()
        buttons.select_hotel(owner,username)
    def registration():
        root.destroy()
        register.start()
    def owner_det():
        owner.clear()
        sql="SELECT * FROM `owner` where aadhar = %s AND state = %s"
        val=(username,"active")
        cur.execute(sql,val)
        result=cur.fetchall()
        for o in result:
            owner[o[3]]={"id":o[0],"password":o[4],"name":o[5],"contact_no":o[6],"state":o[7]}
    #owner_det()        
    #print(owner)
           
    root = tk.Tk()
    frm = ttk.Frame(root, padding=100,borderwidth=3, relief="solid")
    frm.grid()
    ttk.Style().configure('pad.TEntry', padding='5 1 1 1')
    tk.Label(frm,text="Hotel Management",anchor=tk.CENTER,bg="lightblue",height=1,width=20,font=("Arial", 16, "bold"),fg="red",padx=15,pady=15,justify=tk.CENTER,wraplength=200).grid(column=0,row=0)
    '''def click(args):
        unm.delete(0, 'end')'''
    def click(entry):
       # if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')
    def click1(entry):
       # if entry.cget('state') == 'disabled':
            entry.configure(state='normal',show="*")
            entry.delete(0, 'end')        
    def leave(entry,placeholder):    
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(foreground="black")
    unm=ttk.Entry(frm, style='pad.TEntry',width=30)
    unm.grid(column=0, row=2,padx=150,pady=2)
    unm.insert(0, 'username or aadhar')
    unm_click = unm.bind('<Button-1>', lambda x: click(unm))
    unm_leave = unm.bind('<FocusOut>', lambda x: leave(unm, 'username or aadhar'))
    pas=ttk.Entry(frm,style='pad.TEntry',width=30)
    pas.grid(column=0, row=4,padx=150,pady=2)
    pas.insert(0, 'password')
    def login():
        global username
        username = unm.get()
        password = pas.get()
        if username == "" or username == "username or aadhar":
            msg=Message(frm, text = "Enter username",width=200,fg="red")
            msg.grid(column=0,row=7) 
        else:    
            if password == "" or password == "password":
                msg=Message(frm,text="Enter password",width=200,fg="red")
                msg.grid(column=0,row=7 )
            else:   
                sql="select aadhar from owner where aadhar = %s"
                val=(username,)
                cur.execute(sql,val)
                result=cur.fetchone()
                u=result[0]
                print(u)
                if result:
                    username = u
                    sql1="select password from owner where aadhar = %s"
                    val1=(username,)
                    cur.execute(sql1,val1)
                    result1=cur.fetchone()
                    p=result1[0]
                    if password==p:
                        msg=Message(frm,text="login successfully",width=250,fg="green")
                        msg.grid(column=0,row=7)
                        owner_det() 
                        #print(owner)
                        choose_hotel(username)
                    else:
                        #print("Invalid password")
                        msg=Message(frm,text="Invalid password",width=250,fg="red")
                        msg.grid(column=0,row=7)
                else:
                    msg=Message(frm,text="Invalid username",width=250,fg="red")
                    msg.grid(column=0,row=7)
    pas_click = pas.bind('<Button-1>', lambda x: click1(pas))
    pas_leave = pas.bind('<FocusOut>', lambda x: leave(pas, 'password'))    
    tk.Button(frm, text="login", command=login,bg="green",activebackground="blue",activeforeground="white",fg="white",width=10).grid(column=0, row=5,padx=100,pady=2)
    tk.Button(frm, text="register", command=registration,bg="green",activebackground="blue",activeforeground="white",fg="white",width=10).grid(column=0, row=6,padx=100,pady=2)

    root.mainloop()
log_in()    