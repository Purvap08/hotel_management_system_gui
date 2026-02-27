import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector  
from datetime import date
#from tkinter import messagebox 
from tkinter import Message
import time
import re
import register
import buttons
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
owner={}
def choose_hotel(username):
    root.destroy()
    buttons.select_hotel(owner,username)
def registration():
    root.destroy()
    register.start()
def owner_det():
    owner.clear()
    sql="SELECT * FROM `owner` where state = %s"
    val=("active",)
    cur.execute(sql,val)
    result=cur.fetchall()
    for o in result:
        owner[o[3]]={"id":o[0],"password":o[4],"name":o[5],"contact_no":o[6],"state":o[7]}
owner_det()        
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
'''def leave(args):
    unm.delete(0, 'end')
    unm.insert(0, 'username or aadhar')
    root.focus()'''
def leave(entry,placeholder):    
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(foreground="black")
#tk.Label(frm,text='Enter your username').grid(column=0,row=1,padx=100,pady=2)
unm=ttk.Entry(frm, style='pad.TEntry',width=30)
unm.grid(column=0, row=2,padx=150,pady=2)
unm.insert(0, 'username or aadhar')
#unm.bind("<Button-1>",click)
#unm.configure(state='disabled')
#unm.bind("<Leave>", leave)
unm_click = unm.bind('<Button-1>', lambda x: click(unm))
unm_leave = unm.bind('<FocusOut>', lambda x: leave(unm, 'username or aadhar'))
'''def click1(*args):
    pas.delete(0, 'end')
def leave1(*args):
    pas.delete(0, 'end')
    pas.insert(0, 'password')
    root.focus()'''
#tk.Label(frm,text='Enter Password').grid(column=0,row=3,padx=100,pady=2)
pas=ttk.Entry(frm,style='pad.TEntry',width=30)
pas.grid(column=0, row=4,padx=150,pady=2)
pas.insert(0, 'password')
#pas.bind("<Button-1>",click)
#pas.configure(state='disabled')
#pas.bind("<Leave>", leave1)
def login():
    global username
    #frm = ttk.Frame(root, padding=10,borderwidth=3, relief="solid")
    #frm.grid()
    username = unm.get()
    password = pas.get()
    if username == "" or username == "username or aadhar":
        #print("Please Enter username")
        msg=Message(frm, text = "Enter username",width=200,fg="red")
        msg.grid(column=0,row=7) 
        #messagebox.showwarning("showwarning", "Warning") 
    else:    
        if password == "" or password == "password":
            #print("Please Enter the password")
            msg=Message(frm,text="Enter password",width=200,fg="red")
            msg.grid(column=0,row=7 )
            #return
        else:    
            if username in owner:
                if password == owner[username]["password"]:
                    #print("login successfully")
                    msg=Message(frm,text="login successfully",width=250,fg="green")
                    msg.grid(column=0,row=7)
                    #root.destroy() 
                    choose_hotel(username)
                else:
                    #print("Invalid password")
                    msg=Message(frm,text="Invalid password",width=250,fg="red")
                    msg.grid(column=0,row=7)
            else:
                #print("Invalid Username")
                msg=Message(frm,text="Invalid username",width=250,fg="red")
                msg.grid(column=0,row=7)
       
pas_click = pas.bind('<Button-1>', lambda x: click1(pas))
pas_leave = pas.bind('<FocusOut>', lambda x: leave(pas, 'password'))    
tk.Button(frm, text="login", command=login,bg="green",activebackground="blue",activeforeground="white",fg="white",width=10).grid(column=0, row=5,padx=100,pady=2)
tk.Button(frm, text="register", command=registration,bg="green",activebackground="blue",activeforeground="white",fg="white",width=10).grid(column=0, row=6,padx=100,pady=2)

root.mainloop()

#print(unm)
'''if username in owner:
    print(yes)
else:
    print("No")'''