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
menu_c=[]
mcat=[]
mcatnm=[]
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
m_name=[] 
menu_id=[]     
def menu_l(selected_id,owner,username):
    sql="SELECT * FROM `menu` WHERE `owner_id` = %s AND `hotel_id` = %s"
    val=(owner[username]["id"],selected_id)
    cur.execute(sql,val)
    result=cur.fetchall()
    for m in result:
        m_nm[m[0]]={"category_id":m[5],"hotel_id":m[4],"name":m[6],"price":m[7],"status":m[8]}
        m_name.append({"id":m[0],"name":m[6],"price":m[7]})
        menu_id.append(m[0])
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
    for v in menu_c:
        table.insert(parent='', index="end", values=(v["id"], v["name"]))
    table.pack(expand=True, fill=tk.BOTH)
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).pack(padx=10,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).pack(padx=5,pady=5)
    root.mainloop()  
def add_menu(selected_id,owner,username):
    menu_cat(selected_id,owner,username)
    menu_l(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Add menu")
    frm=tk.Frame(root,width=500,height=500)
    frm.grid(row=0,column=0)
    tk.Label(frm,text="Add Menu",bg="sky blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=0,columnspan=2,pady=10)
    table=ttk.Treeview(root)
    table['columns']=('Id','Name')
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Id', anchor=tk.W, width=150)
    table.column('Name', anchor=tk.W, width=200)
    table.heading('#0', text='', anchor=tk.W)
    table.heading('Id', text='Id', anchor=tk.W)
    table.heading('Name', text='Name', anchor=tk.W)
    for v in menu_c:
        table.insert(parent='', index="end", values=(v["id"], v["name"]))
    table.grid(row=1, column=0, columnspan=2, sticky="new", pady=10)
    tk.Label(frm,text="Enter Category Id:").grid(row=2,column=0,pady=10)
    c_id=tk.Entry(frm,width=50)
    c_id.grid(row=2,column=1,pady=10)
    tk.Label(frm,text="Enter Item name:").grid(row=4,column=0,pady=10)
    menu_nm=tk.Entry(frm,width=50)
    menu_nm.grid(row=4,column=1,pady=10)
    tk.Label(frm,text="Enter Price").grid(row=6,column=0)
    m_pr=tk.Entry(frm,width=50)
    m_pr.grid(row=6,column=1)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)
    def add_m():
        cid=c_id.get()
        if cid == "":
            tk.Message(frm,text="Enter category Id",fg="red",bg="white",width=200).grid(row=7,column=1,columnspan=2)
        if not cid.isdigit() or int(cid) not in mcat:
            tk.Message(frm,text="Invalid Category Id",fg="red",bg="white",width=200).grid(row=7,column=1,columnspan=2)
        else:
            #r=0
            mnm=menu_nm.get()
            r=0    
            for m in m_nm.values():
                if mnm == m["name"]:
                    #print("yes")
                    r=1
                    break
                    #return
            if mnm == "":
                tk.Message(frm,text="Enter Item name",bg="white",fg="red",width=200).grid(row=7,column=1,columnspan=2)        
            elif r:        
                tk.Message(frm,text="Item name is already added",bg="white",fg="red",width=200).grid(row=7,column=1,columnspan=2)
                #return       
            else:
                mpr = m_pr.get()
                if mpr == "":
                    tk.Message(frm,text="Enter Item Price",bg="white",fg="red",width=200).grid(row=7,column=1,columnspan=2)
                elif  not mpr.isdigit() or int(mpr) <= 0:
                    tk.Message(frm,text="Enter valid price",bg="white",fg="red",width=200).grid(row=7,column=1,columnspan=2)
                else:
                    tk.Message(frm,text="Menu Item added Successfully",bg="white",fg="green",width=200).grid(row=7,column=1,columnspan=2)
                    c_id.delete(0,tk.END)
                    menu_nm.delete(0,tk.END)
                    m_pr.delete(0,tk.END)
                    sql="INSERT INTO `menu` (`date`,`time`,`owner_id`,`hotel_id`,`category_id`,`name`,`price`,`status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(d,t,owner[username]["id"],selected_id,cid,mnm,mpr,"available")
                    cur.execute(sql,val)
                    db.commit()
                #tk.Button(frm,text="Add",command=price,fg="white",bg="green",width=10).grid(row=8,column=0)        
        menu_l(selected_id,owner,username)            
            #tk.Button(frm,text="save",command=mname,fg="white",bg="green",activebackground="blue").grid(row=4,column=2,pady=10)
        #table.grid(row=1, column=0, columnspan=2, sticky="new", pady=10)
    tk.Button(frm,text="Update",command=add_m,fg="white",bg="green",activebackground="blue").grid(row=8,column=0,pady=10)
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).grid(row=8,column=1,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).grid(row=8,column=2,pady=10)
    root.mainloop()
def check_m(selected_id,owner,username):
    menu_l(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Check Menu")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=0,column=0)
    #frm.grid(row=1,column=1)
    frm.pack(padx=10,pady=10)
    #print(menu_c)
    tk.Label(frm,text="Check Menu",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).pack(padx=10,pady=10)
    table=ttk.Treeview(root)
    table['columns']=('Id','Name','price')
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Id', anchor=tk.W, width=150)
    table.column('Name', anchor=tk.W, width=200)
    table.column('price', anchor=tk.W, width=250)
    
    table.heading('#0', text='', anchor=tk.W)
    table.heading('Id', text='Id', anchor=tk.W)
    table.heading('Name',text='Name',anchor=tk.W)
    table.heading('price',text="Price",anchor=tk.W)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)    
    for v in m_name:
        table.insert(parent='', index="end", values=(v["id"], v["name"] ,v["price"]))
    table.pack(expand=True, fill=tk.BOTH)
    m_name.clear()
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).pack(padx=10,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).pack(padx=5,pady=5)
    root.mainloop()
def delete_m(selected_id,owner,username):
    menu_l(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Delete Menu")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=1,column=1)
    frm.grid(row=0,column=0)
    #print(menu_c)
    tk.Label(frm,text="Delete Menu",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=0,columnspan=2,pady=10)
    table=ttk.Treeview(root)
    table['columns']=('Id','Name','price')
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Id', anchor=tk.W, width=150)
    table.column('Name', anchor=tk.W, width=200)
    table.column('price', anchor=tk.W, width=250)
    
    table.heading('#0', text='', anchor=tk.W)
    table.heading('Id', text='Id', anchor=tk.W)
    table.heading('Name', text='Name', anchor=tk.W)
    table.heading('price',text="Price",anchor=tk.W)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)    
    for v in m_name:
        table.insert(parent='', index="end", values=(v["id"], v["name"] ,v["price"]))
    table.grid(row=1, column=0, columnspan=2, sticky="new", pady=10)
    m_name.clear()
    tk.Label(frm,text="Enter Menu Id:").grid(row=2,column=0,pady=10)
    m_id=tk.Entry(frm,width=50)
    m_id.grid(row=2,column=1,pady=10)
    def delete():
        mid=m_id.get()
        if mid == "":
            tk.Message(frm,text="Enter Menu Id",bg="white",fg="red",width=200).grid(row=3,column=1,columnspan=2)  
        elif not mid.isdigit() or int(mid) not in menu_id:
            tk.Message(frm,text="Invalid menu Id",bg="white",fg="red",width=200).grid(row=3,column=1,columnspan=2)
        else:
            sql="DELETE FROM `menu` WHERE id = %s"
            val=(mid,)
            cur.execute(sql,val)
            db.commit()
            tk.Message(frm,text="Item deleted Successfully",bg="white",fg="green",width=200).grid(row=3,column=1,columnspan=2)
            m_id.delete(0,tk.END)
    tk.Button(frm,text="Delete",command=delete,bg="green",fg="white",activebackground="blue",width=10).grid(row=8,column=0,pady=10)    
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).grid(row=8,column=1,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).grid(row=8,column=2,pady=10)
    root.mainloop()
def update_m():
    menu_l(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Update Menu")
    frm=tk.Frame(root,width=500,height=500)
    #frm.grid(row=1,column=1)
    frm.grid(row=0,column=0)
    #print(menu_c)
    tk.Label(frm,text="Update Menu",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=0,columnspan=2,pady=10)
    table=ttk.Treeview(root)
    table['columns']=('Id','Name','price')
    table.column('#0', width=0, stretch=tk.NO)
    table.column('Id', anchor=tk.W, width=150)
    table.column('Name', anchor=tk.W, width=200)
    table.column('price', anchor=tk.W, width=250)
    
    table.heading('#0', text='', anchor=tk.W)
    table.heading('Id', text='Id', anchor=tk.W)
    table.heading('Name', text='Name', anchor=tk.W)
    table.heading('price',text="Price",anchor=tk.W)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)    
    for v in m_name:
        table.insert(parent='', index="end", values=(v["id"], v["name"] ,v["price"]))
    table.grid(row=1, column=0, columnspan=2, sticky="new", pady=10)
    m_name.clear()
    