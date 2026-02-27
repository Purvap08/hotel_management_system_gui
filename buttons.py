import mysql.connector
import tkinter as tk
from tkinter import *
db=mysql.connector.connect(
		host="Localhost",
		user="root",
		password="",
		database="hotel_management",
		#port=""
)
cur=db.cursor()
#print(db)
def select_hotel(owner,username):
    hotel={}
    def hotel_det():
        sql="select * from hotels where owner_id = %s AND state = %s"
        val=(owner[username]["id"],"active")
        cur.execute(sql,val)
        result=cur.fetchall()
        #print(result)
        for h in result:
            hotel[h[0]]={"owner_id":h[3],"hotel_name":h[4],"status":h[5]}
    hotel_det()    
    #print(hotel)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("dashboard")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=2,column=1)
    frm.pack(padx=5,pady=5)
    #tk.Label(frm,text="Hotel Management System",bg="red",fg="white").grid(row=0,column=5)
    tk.Label(frm,text="Hotel Management System",bg="red",fg="white",width=50,height=3,font=("Arial",16,"bold")).pack(padx=20,pady=50)
    tk.Button(frm,text="Hotel",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="35",relief="flat").pack(padx=10,pady=10)
    #tk.Button(frm,text="Menu Category",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="40").pack(padx=5,pady=5)
    #tk.Button(frm,text="Menu",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="40").pack(padx=5,pady=5)
    menubutton = Menubutton(frm, text="Select Hotel",bg="sky blue",activebackground="light green",fg="white",width="40")
    menubutton.pack(padx=5,pady=5)
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]= menubutton.menu
    for h1,hnm in hotel.items():
        menubutton.menu.add_checkbutton(label=hnm["hotel_name"])
    root.mainloop()