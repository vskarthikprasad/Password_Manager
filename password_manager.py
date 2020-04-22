from tkinter import *
import mysql.connector
import tkinter.messagebox
root1=Tk()
root1.geometry("600x500")
root1.configure(bg="black")
root1.title('Login Form')
mydb = mysql.connector.connect(host="localhost",user="root",passwd="%your_password%",auth_plugin='mysql_native_password',database="%your_db%")
mycursor = mydb.cursor()


def new_win():
	n1=mpass.get()
	sqlcmd='select %password_column_name% from %your_master_table% where name="%your column name%"'
	mycursor.execute(sqlcmd)
	myresult=mycursor.fetchone()
	if myresult[0] == n1:
		mpass.delete("0",END)
		root=Toplevel(root1)
		root.geometry("800x400+200+300")
		root.configure(bg="black")
		def insert():
		    v1=uname.get()
		    v2=pswd.get()
		    v0=hst.get()
		    if v0 == "" or v1 == "" or v2 == "":
		        tkinter.messagebox.askretrycancel('Error','Null Input!')
		    else:
		    	sqlcmd='insert into %your_table2% values(%s,%s,%s)'
		    	values=(v0,v1,v2)
		    	mycursor.execute(sqlcmd,values)
		    	mydb.commit()
		    	hst.delete("0",END)
		    	uname.delete("0",END)
		    	pswd.delete("0",END)
		    	tkinter.messagebox.askokcancel('Sucess','Inserted Sucessfully!')

		def show():
			sqlcmd="select * from %your_table2%"
			mycursor.execute(sqlcmd)
			myresult=mycursor.fetchall()
			res=[row for row in myresult]
			lbl3.config(text=res)

		def update():

			v0=hst.get()
			v1=uname.get()
			v2=pswd.get()
			if v0 == "" or v1 == "" or v2 == "":
				tkinter.messagebox.askretrycancel('Error','Null Input')
			else:
				sqlcmd="update %your_table2% set %password_column_name%=%s where %host_column_name%=%s "
				mycursor.execute(sqlcmd,(v2,v0))
				mydb.commit()
				hst.delete("0",END)
				uname.delete("0",END)
				pswd.delete("0",END)
				tkinter.messagebox.askokcancel('Sucess','Updated Sucessfully')
			
		def quit():
			root.destroy()

		lbl0=Label(root,text="Host:",fg="black",bg="lightyellow",font="Helvetica 12 bold")
		lbl1=Label(root,text="Username: ",fg="black",bg="lightyellow",font="Helvetica 12 bold")
		lbl2=Label(root,text="Password: ",fg="black",bg="lightyellow",font="Helvetica 12 bold")
		hst=Entry(root,font="Helvetica 12")
		uname=Entry(root,font="Helvetica 12")
		pswd=Entry(root,show="*",font="Helvetica 12")
		lbl0.place(x=70,y=160,anchor=W)
		lbl1.place(x=70,y=190,anchor=W)
		lbl2.place(x=70,y=220,anchor=W)
		hst.place(x=180,y=160,anchor=W,width="200",height="25")
		uname.place(x=180,y=190,anchor=W,width="200",height="25")
		pswd.place(x=180,y=220,anchor=W,width="200",height="25")
		b1=Button(root,text="Store",command=insert,bg="Aqua",fg="black",font="Helvetica 12 bold")
		b1.place(relx = 0.3, rely = 0.8,anchor=CENTER)
		b2=Button(root,text="Show",command=show,bg="Aqua",fg="black",font="Helvetica 12 bold")
		b2.place(relx = 0.2, rely = 0.8,anchor=CENTER)
		b3=Button(root,text="Update",command=update,bg="Aqua",fg="black",font="Helvetica 12 bold")
		b3.place(relx = 0.4, rely = 0.8,anchor=CENTER)
		b4=Button(root,text="Exit",command=quit,bg="Red",fg="black",font="Helvetica 12 bold")
		b4.place(relx = 0.5, rely = 0.8,anchor=CENTER)
		lbl3=Label(root)
		lbl3.place(x=200,y=170,anchor=CENTER)


	elif n1 == "":
		tkinter.messagebox.askretrycancel('Error','Null Input')
	else:
		tkinter.messagebox.askretrycancel('Error','Invalid Password!')
		mpass.delete("0",END)



lbl0=Label(root1,text="Welcome to My Password Manager",fg="black",bg="Orange",font="Verdana 14 italic")
lbl0.place(x=300,y=120,anchor=CENTER)
lbl1=Label(root1,text="Enter the master password: ",fg="black",bg="lightyellow",font="Helvetica 12 bold")
lbl1.place(x=70,y=200,anchor=W)
mpass=Entry(root1,show="*",font="Helvetica 12")
mpass.place(x=300,y=200,anchor=W,width="200",height="25")
button1 =Button(root1, text ="Check", command =new_win,bg="Aqua",fg="black",font="Helvetica 12 bold") #command linked
button1.place(relx=0.5,rely=0.5,anchor=CENTER,width="100",height="30")
root1.mainloop()




