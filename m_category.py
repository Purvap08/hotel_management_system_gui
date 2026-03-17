import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
from datetime import date
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
mcat=[]
mcatnm=[]
menu_c=[]
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
    #print(menu_c)    
def add_cat(selected_id,owner,username):
    menu_cat(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Add Menu Category")
    frm=tk.Frame(root,width=500,height=500)
    frm.grid(row=1,column=1)
    tk.Label(frm,text="Add Category",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=2)
    tk.Label(frm,text="Enter Category name:").grid(row=1,column=1)
    c=tk.Entry(frm)
    c.grid(row=1,column=2)
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)
    def m_cat():
        cn=c.get()
        if cn == "" :
            msg=Message(frm,text="Enter Menu Category",fg="red",width=200).grid(row=2,column=1)
        r=0    
        for v in menu_c.values():
            if cn == v["name"]:
                r=1
                break
        if r:
            msg=Message(frm,text="Category is Already added",fg="red",width=200).grid(row=2,column=1)
        else:
            sql="INSERT INTO `menu_category` (`date`,`time`,`owner_id`,`hotel_id`,`name`,`status`) VALUES (%s,%s,%s,%s,%s,%s)"
            val=(d,t,owner[username]["id"],selected_id,cn,"available")
            cur.execute(sql,val)
            db.commit()
            time.sleep(2)
            msg=Message(frm,text="Menu Category Added Successfully",fg="green",width=200).grid(row=2,column=1)
            c.delete(0,tk.END)
        menu_cat(selected_id,owner,username)    
    #print(cn)
    tk.Button(frm,text="Sumbit",command=m_cat,bg="green",fg="white",activebackground="blue",width=10).grid(row=4,column=0)
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).grid(row=4,column=1)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).grid(row=4,column=2)
    #add_cat()    
    root.mainloop()
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
def delete(selected_id,owner,username):
    '''check(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Delete Category")
    frm=tk.Frame(root,width=500,height=500)
    frm.pack(padx=10,pady=10)
    #tk.Label(frm,text="Enter Category Id",bg="",fg="",anchor=tk.CENTER,wraplength=200).pack(padx=10,pady=10)
    tk.Label(frm,text="Enter Category Id").pack(padx=10,pady=10)
    root.mainloop()'''
    menu_cat(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Check Menu Category")
    frm=tk.Frame(root,width=500,height=500)
    frm.grid(row=0,column=0,padx=10,pady=10)
    #frm.pack(padx=10,pady=10)
    #print(menu_c)
    tk.Label(frm,text="Delete Category",bg="Sky Blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=0,columnspan=2,pady=10)    
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
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)
    def delete_cat(): 
        cid=c_id.get()
        if cid == "":
            tk.Message(frm,text="Enter Category Id",fg="red",bg="white",width=200).grid(row=3,column=1,columnspan=2)
        elif int(cid) not in mcat:
            tk.Message(frm,text="Invalid Category Id",fg="red",bg="white",width=200).grid(row=3,column=1,columnspan=2)   
        else:
            sql="DELETE FROM `menu_category` WHERE `id` = %s"
            val=(cid,)
            cur.execute(sql,val)
            db.commit()
            tk.Message(frm,text="Category deleted Successfully",bg="white",fg="green",width=200).grid(row=3,column=1,columnspan=2)
            c_id.delete(0,tk.END) 
    tk.Button(frm,text="Delete",command=delete_cat,fg="white",bg="red",activebackground="blue",width=10).grid(row=4,column=0,pady=10)    
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).grid(row=4,column=1,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).grid(row=4,column=2,pady=10)
    frm.grid_rowconfigure(1, weight=1)
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_columnconfigure(1, weight=1)
    root.mainloop()
def update(selected_id,owner,username):
    menu_cat(selected_id,owner,username)
    root=tk.Tk()
    root.geometry("600x600")
    root.title("Update Category")
    frm=tk.Frame(root,width=500,height=500)
    frm.grid(row=0,column=0)
    tk.Label(frm,text="Update Category",bg="sky blue",fg="white",anchor=tk.CENTER,wraplength=200,width=30).grid(row=0,column=0,columnspan=2,pady=10)
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
    def back():
        root.destroy()
        select_hotels.update(selected_id,owner,username)
    def update_cat():
        cid=c_id.get()
        if cid == "":
            tk.Message(frm,text="Enter Category Id",fg="red",bg="white",width=200).grid(row=3,column=1,columnspan=2)
        elif int(cid) not in mcat:
            tk.Message(frm,text="Invalid Category Id",fg="red",bg="white",width=200).grid(row=3,column=1,columnspan=2)
        else:
            tk.Label(frm,text="Enter category name:").grid(row=4,column=0,pady=10)
            c_nm=tk.Entry(frm,width=50)
            c_nm.grid(row=4,column=1,pady=10)
            def save_update():
                cnm=c_nm.get()
                if cnm == "":
                    tk.Message(frm,text="Enter Category name",bg="white",fg="red",width=200).grid(row=5,column=1,columnspan=2)
                elif cnm in mcatnm:
                    tk.Message(frm,text="Category is already Exists",bg="white",fg="red",width=200).grid(row=5,column=1,columnspan=2)
                else:
                    sql="UPDATE `menu_category` SET name = %s WHERE id = %s"
                    val=(cnm,cid)
                    cur.execute(sql,val)
                    db.commit()
                    tk.Message(frm,text="Category Updated Successfully",bg="white",fg="green",width=200).grid(row=6,column=1,columnspan=2)
                    c_id.delete(0,tk.END)
                    c_nm.delete(0,tk.END)
            tk.Button(frm, text="Save", command=save_update, fg="white", bg="green").grid(row=4, column=2, pady=10)    
                    
    tk.Button(frm,text="Update",command=update_cat,fg="white",bg="green",activebackground="blue",width=10).grid(row=7,column=0,pady=10)
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).grid(row=7,column=1,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).grid(row=7,column=2,pady=10)
    root.mainloop()
