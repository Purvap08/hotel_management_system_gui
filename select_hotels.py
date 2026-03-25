import mysql.connector
import tkinter as tk
from tkinter import *
import buttons
import logout1
import m_category
import menu
db=mysql.connector.connect(
    host="Localhost",
    user="root",
    password="",
    database="Hotel_management"
    #port=""
)
cur=db.cursor()
#print(db)
def update(selected_id,owner,username):
    root=tk.Tk()
    root.geometry("600x1000")
    root.title("Update hotel")
    frm=tk.Frame(root,width=500,height=500)
    frm.pack(padx=10,pady=10)
    sql="SELECT `hotel_name` FROM `hotels` WHERE id = %s"
    val=(selected_id,)
    cur.execute(sql,val)
    result=cur.fetchone()
    #print(result)
    tk.Label(frm,text=f"Welcome to {result[0]}",bg="red",fg="white",width=50,height=2,font=("Arial",18,"bold")).pack(padx=10,pady=10)
    v=StringVar(frm,"1")
    o_frm=tk.Frame(frm,width=200,height=200)
    o_frm.pack(padx=10,pady=10,fill=X)
    def clear_o():
        #print(o_frm.winfo_children())
        for x in o_frm.winfo_children():
            x.destroy()
    def back():
        root.destroy()
        buttons.select_hotel(owner,username)
    def c_add():
        root.destroy()
        m_category.add_cat(selected_id,owner,username)
    def c_check():
        root.destroy()
        m_category.check(selected_id,owner,username)
    def c_delete():
        root.destroy()
        m_category.delete(selected_id,owner,username)
    def c_update():
        root.destroy()
        m_category.update(selected_id,owner,username)
    def m_add():
        root.destroy()
        menu.add_menu(selected_id,owner,username)
    def m_check():
        root.destroy()
        menu.check_m(selected_id,owner,username)
    def m_delete():
        root.destroy()
        menu.delete_m(selected_id,owner,username)
    def menu_c_o():
        clear_o()
        Radiobutton(o_frm,text="Add Category",command=c_add,variable = v,value="21",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Delete Category",command=c_delete,variable= v,value="2",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Update Category",command=c_update,variable= v,value="3",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Check menu Category",command=c_check,variable=v,value="4",indicator=0,background="light pink").pack(fill=X,ipady=5)
    def menu_o():
        clear_o()
        Radiobutton(o_frm,text="Add menu",command=m_add,variable= v,value="5",indicator=0,background="light pink").pack(fill= X,ipady=5)
        Radiobutton(o_frm,text="Delete menu",command=m_delete,variable= v,value="6",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Update menu",variable= v,value="7",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Check menu",command=m_check,variable=v,value="8",indicator=0,background="light pink").pack(fill=X,ipady=5)
    def chef_o():
        clear_o()
        Radiobutton(o_frm,text="Add Chef",variable= v,value="9",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Delete Chef",variable=v,value="10",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Update Chef",variable=v,value="11",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Check Chef",variable=v,value="12",indicator=0,background="light pink").pack(fill=X,ipady=5)
    def wait_o():
        clear_o()
        Radiobutton(o_frm,text="Add Waiter",variable=v,value="13",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Delete Waiter",variable=v,value="14",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Update Waiter",variable=v,value="15",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Check Waiter",variable=v,value="16",indicator=0,background="light pink").pack(fill=X,ipady=5)
    def table_o():
        clear_o()
        Radiobutton(o_frm,text="Add Table",variable=v,value="17",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Delete Table",variable=v,value="18",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Update Table",variable=v,value="19",indicator=0,background="light pink").pack(fill=X,ipady=5)
        Radiobutton(o_frm,text="Check Table",variable=v,value="20",indicator=0,background="light pink").pack(fill=X,ipady=5)
    def order_o():
        clear_o()
        #Radiobutton(frm,text="Add Table",variable=v,value="16",indicator=0,background="light pink").pack(fill=X,ipady=5)
        #Radiobutton(frm,text="Delete Table",variable=v,value="17",indicator=0,background="light pink").pack(fill=X,ipady=5)
        #Radiobutton(frm,text="Add Table",variable=v,value="18",indicator=0,background="light pink").pack(fill=X,ipady=5)    
    tk.Button(frm,text="Menu Category",command=menu_c_o,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Menu Items",command=menu_o,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Chef",command=chef_o,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Waiter",command=wait_o,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Tables",command=table_o,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Order",command=root.destroy,bg="sky blue",fg="white",width=35,relief="flat").pack(padx=10,pady=10)
    tk.Button(frm,text="Back",command=back,bg="red",fg="white",activebackground="blue",width=10).pack(padx=10,pady=10)
    tk.Button(frm,text="Logout",command=lambda:logout1.log_out(root),bg="red",fg="white",activebackground="blue",width=10).pack(padx=10,pady=10)
    root.mainloop()
#update(selected_id,owner,username)    