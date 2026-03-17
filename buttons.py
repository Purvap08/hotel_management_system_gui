import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import Message
import add_hotel
import logout1
import select_hotels
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
    def ad_hotel():
        root.destroy()
        add_hotel.start(owner,username)
    #print(hotel)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("dashboard")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=2,column=1)
    frm.pack(padx=5,pady=5)
    #tk.Label(frm,text="Hotel Management System",bg="red",fg="white").grid(row=0,column=5)
    tk.Label(frm,text=f"Welcome {owner[username]['name']}",bg="red",fg="Yellow",width=50,font=("Arial",16,"bold")).pack(padx=5,pady=5)
    tk.Label(frm,text="Hotel Management - Dashboard",bg="red",fg="white",width=50,font=("Arial",12,"bold")).pack(padx=5,pady=5)
    tk.Button(frm,text="Add Hotel",command=ad_hotel,bg="sky blue",activebackground="light green",fg="white",width="35",relief="flat").pack(padx=10,pady=10)
    #tk.Button(frm,text="Menu Category",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="40").pack(padx=5,pady=5)
    #tk.Button(frm,text="Menu",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="40").pack(padx=5,pady=5)
    '''menubutton = Menubutton(frm, text="Select Hotel",bg="sky blue",activebackground="light green",fg="white",width="40")
    menubutton.pack(padx=5,pady=5)
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]= menubutton.menu
    #hotel_vars={}
    for h1,hnm in hotel.items():
        #print(hnm["hotel_name"])
        var=IntVar()
        #hotel_vars[h1]=var
        menubutton.menu.add_checkbutton(label=hnm["hotel_name"],variable=var)'''
    #print(hotel_vars)
    selected_hotel = tk.StringVar()
    def s_hotel():
        v = StringVar(frm, "1")   
        for h1,hnm in hotel.items():
            #print(hnm["hotel_name"])
            #var=IntVar()
            #hotel_vars[h1]=var
            Radiobutton(frm, text = hnm["hotel_name"], variable = selected_hotel, value = str(h1), indicator = 0,background = "light blue").pack(fill = X, ipady = 5)
    def sel_hotel():
        global selected_id
        selected_id = selected_hotel.get()
        if selected_id == "":
            print("No hotel selected")
            msg=Message(frm, text="Please select a hotel", fg="red")
            msg.pack(padx=10,pady=10)
            return
            select_hotels.update(selected_id,owner,username)
        '''for h1,hnm in hotel.items():
            if hnm.get(h1) == 1:
                selected_hotel.append[h1,hnm]'''
        #print(selected_id)  
        #print(hotel[int(selected_id)]["hotel_name"])
    def hotel_s():
        global selected_id
        selected_id = selected_hotel.get()
        if selected_id == "":
            msg=Message(frm,text="No hotel is selected",fg="red",width="250")
            msg.pack(padx=10,pady=10)
        else:    
            root.destroy()
            sel_hotel()
            select_hotels.update(selected_id,owner,username)
        
    #tk.Button(frm,text="cancel",command=root.destroy,bg="sky blue",activebackground="light green",fg="white",width="35",relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Select Hotel",command=s_hotel,bg="sky blue",activebackground="green",fg="white",width="35",relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Submit",command=hotel_s,bg="sky blue",activebackground="green",fg="white",width="35",relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="sky blue",activebackground="red",fg="white",width="35",relief="flat").pack(padx=10,pady=10)  
    #print(var) 
    root.mainloop()