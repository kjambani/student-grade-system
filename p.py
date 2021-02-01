from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


class roll(Exception):
	def __init__(self,rno):
		self.r=rno
class na(Exception):
	def __init__(self,rno):
		self.r=rno
class ma(Exception):
	def __init__(self,rno):
		self.r=rno
class rollup(Exception):
	def __init__(self,rno):
		self.r=rno



root=Tk()
root.iconbitmap(r'D:\Demo\Python\Project\sms.ico')
root.title("SMS")
root.geometry("500x650+300+300")

def f1():
	root.withdraw()
	addst.deiconify()
def f2():
	addst.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	viewst.deiconify()
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg + "r: "+str(d[0])+ " n: " +str(d[1]) + " m: " +str(d[2]) + "\n"
		stData.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		print("Issues " ,e)
	finally:
		if cursor is not None:
			cursor.close()	
		if con is not None:
			con.close()
			print("disconnected")
def f4():
	viewst.withdraw()
	root.deiconify()
	stData.delete(0.0,END)

def f5():
	import cx_Oracle
	con=None
	cursor=None
	try:    
		con=cx_Oracle.connect("system/abc123")
		rno=int(entRno.get())
		if rno < 0:
			raise roll(rno)

	except rollup as r:
		messagebox.showerror('ERROR',"This Roll no does not exists in database")
		entRNo1.delete(0,END)
		entRno1.focus()
	except roll as r:
		messagebox.showerror('ERROR',"Please IInsert posivtive integers")
		entRno1.delete(0,END)
		entRno1.focus()
	
		
	except ValueError :
		messagebox.showerror('ERROR',"Please insert integers only")
		entRno1.delete(0,END)
		entRno1.focus()
		#con.rollback()
	except:
		messagebox.showerror('ERROR',"Issues")
		entRno1.delete(0,END)
		entRno1.focus()
		#con.rollback()

	try:
		name= entName.get()
		if len(name) < 2:
			raise na(name)
	except ValueError :
		messagebox.showerror('galat',"please insert intgers only")
		entryname.delete(0,END)
		entryname.focus()
		#con.rollback()
	except na :
		messagebox.showerror('galat',"name should atleast contain two letters")
		entryname.delete(0,END)
		entryname.focus()
		#con.rollback()
	except:
		messagebox.showerror('galat',"some thing is wrong")
		entryname.delete(0,END)
		entryname.focus()
		#con.rollback()
	try:
		marks= int(entMarks.get())
		if marks > 100:
			raise ma(marks)
		if marks < 0 :
			raise ma(marks)
	except ValueError :
		messagebox.showerror('galat',"please insert intgers only")
		entryma.delete(0,END)
		entryma.focus()
		#con.rollback()
	except ma :
		messagebox.showerror('galat',"marks should be between 0 to 100")
		entryma.delete(0,END)
		entryma.focus()
		#con.rollback()
	except:
		messagebox.showerror('galat',"some thing is wrong")
		entryma.delete(0,END)
		entryma.focus()
		#con.rollback()
	else:
		try:
			con = cx_Oracle.connect("system/abc123")

			cursor=con.cursor()
			sql="insert into student values('%d','%s', '%d')"
			args=(rno,name,marks)
			cursor.execute(sql%args)
			con.commit()
			msg=str(cursor.rowcount)+ "records inserted"
			messagebox.showinfo("Correct Result ",msg)
			entRno.delete(0,END)
			entName.delete(0,END)
			entMarks.delete(0,END)
		except cx_Oracle.DatabaseError as e:
			messagebox.showerror("Issues " ,e)
			con.rollback()
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close
def f6():
	root.withdraw()
	upst.deiconify()
def f7():
	upst.withdraw()
	root.deiconify()
def f8():
	root.withdraw()
	delst.deiconify()
def f9():
	delst.withdraw()
	root.deiconify()
def f10():
	root.withdraw()
	grst.deiconify()
def f11():
	grst.withdraw()
	root.deiconify()
def f12():
	import cx_Oracle
	con=None
	cursor=None
	try:    
		con=cx_Oracle.connect("system/abc123")
		rno=int(entRno1.get())
		cursor=con.cursor()
		i=(rno,)
		s1= "select rno from student"
		cursor.execute(s1)
		rnodata = cursor.fetchall()
		if i not in rnodata:
			raise rollup(rno)
		
		if rno < 0:
			raise roll(rno)

	except rollup as r:
		messagebox.showerror('ERROR',"This Roll no does not exists in database")
		entRNo1.delete(0,END)
		entRno1.focus()
	except roll as r:
		messagebox.showerror('ERROR',"Please IInsert posivtive integers")
		entRno1.delete(0,END)
		entRno1.focus()
	
		
	except ValueError :
		messagebox.showerror('ERROR',"Please insert integers only")
		entRno1.delete(0,END)
		entRno1.focus()
		#con.rollback()
	except:
		messagebox.showerror('ERROR',"Issues")
		entRno1.delete(0,END)
		entRno1.focus()
		#con.rollback()
	try:
		marks=int(entMarks1.get())
		if marks > 100:
			raise ma(marks)
		if marks < 0 :
			raise ma(marks)
	except ma :
		messagebox.showerror('ERROR',"Marks should be in range from 0 to 100")
		entMarks1.delete(0,END)
		entMarks1.focus()
		#con.rollback()
	
	except ValueError :
		messagebox.showerror('ERROR',"Please insert integers only")
		entMarks1.delete(0,END)
		entMarks1.focus()
		#con.rollback()
	except:
		messagebox.showerror('ERROR',"Issues")
		entMarks1.delete(0,END)
		entMarks1.focus()
		#con.rollback()
		
	else:
		try:
			sql="update student set marks='%d' where rno='%d'"
			args=(marks,rno)
			cursor.execute(sql%args)
			con.commit()
			msg="record updated"
			messagebox.showinfo("Correct Result ",msg)
			entRno1.delete(0,END)
			entMarks1.delete(0,END)
		except cx_Oracle.DatabaseError as e:
			messagebox.showerror("Issues " ,e)
			con.rollback()
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close
def f13():
	import cx_Oracle
	con=None
	cursor=None
	try:    
		con=cx_Oracle.connect("system/abc123")
		rno=int(entRno2.get())
		cursor=con.cursor()
		sql="delete from student where rno='%d'"
		args=(rno)
		cursor.execute(sql%args)
		con.commit()
		msg="record deleted"
		messagebox.showinfo("Correct Result ",msg)
		entRno1.delete(0,END)
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Issues " ,e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close
def f14():
	import cx_Oracle
	from matplotlib import pyplot as plt
	from operator import itemgetter
	import numpy as np
	con = None
	cursor = None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		#print(data)
		names = list(map(itemgetter(1),data))
		#print(names) 
		marks = list(map(itemgetter(2),data))
		x=np.arange(len(names))
		plt.title('student vs marks')
		plt.bar(x,marks,width=0.25,label="marks")
		plt.xticks(x,names,fontsize=7)
		plt.xlabel("Students")
		plt.ylabel('Marks')
		plt.grid()
		plt.legend()
		plt.show()
		
		
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('ERROR',e)
	finally:
		if con is not None:
			con.close()
def f15():
	import cx_Oracle
	from matplotlib import pyplot as plt
	from operator import itemgetter
	import numpy as np
	con = None
	cursor = None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		#print(data)
		names = list(map(itemgetter(1),data))
		#print(names) 
		marks = list(map(itemgetter(2),data))
		plt.plot(names,marks,linewidth=3,label="STUDENT",marker='o',markersize=10)
		plt.xlabel("NAME")	
		plt.ylabel("MARKS")
		plt.title("STATISTICS")
		plt.grid()
		plt.grid()
		plt.show()

		
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('ERROR',e)
	finally:
		if con is not None:
			con.close()
def f16():
	import cx_Oracle
	import pandas as pd
	from matplotlib import pyplot as plt
	from operator import itemgetter
	import numpy as np
	con = None
	cursor = None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		#print(data)
		names = list(map(itemgetter(1),data))
		#print(names) 
		marks = list(map(itemgetter(2),data))
		plt.axis("equal")
		plt.pie(marks,labels=names,radius=1.1,shadow=True,autopct='%.2f%%')
		#colors=['r','#0000ff','g','teal'],
		plt.show()
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror('ERROR',e)
	finally:
		if con is not None:
			con.close()
def f17():
	root.withdraw()
	grst.deiconify()
	
def f18():
	grst.withdraw()
	root.deiconify()
	

btnadd=Button(root,text="ADD",width=10,font=("Arial",18,"italic"),command=f1)
btnview=Button(root,text="VIEW",width=10,font=("Arial",18,"italic"),command=f3)
btnup=Button(root,text="UPDATE",width=10,font=("Arial",18,"italic"),command=f6)
btndel=Button(root,text="DELETE",width=10,font=("Arial",18,"italic"),command=f8)
btngr=Button(root,text="GRAPH",width=10,font=("Arial",18,"italic"),command=f17)

lblqot=Label(text="QOTD",font=("Arial",18,"italic"))
entqot=Entry(root,bd = 7,width=50)
lbltemp=Label(text="TEMP",font=("Arial",18,"italic"))
enttemp=Entry(root,bd = 7,width=50)
btnadd.pack(pady=10)
btnview.pack(pady=10)
btnup.pack(pady=10)
btndel.pack(pady=10)
btngr.pack(pady=10)
lblqot.pack(pady=10)
entqot.pack(pady=10)
lbltemp.pack(pady=10)
enttemp.pack(pady=10)


addst=Toplevel(root)
addst.title("ADD STUDENT")
addst.geometry("400x500+300+200")
addst.withdraw()
lblRno=Label(addst,text="Enter Number",font=("Arial",18,"italic"))
entRno=Entry(addst,bd=5,font=("Arial",18,"italic"))
lblName=Label(addst,text="Enter Name",font=("Arial",18,"italic"))
entName=Entry(addst,bd=5,font=("Arial",18,"italic"))
lblMarks=Label(addst,text="Enter Marks",font=("Arial",18,"italic"))
entMarks=Entry(addst,bd=5,font=("Arial",18,"italic"))

btnaddsave=Button(addst,text="SAVE",width=10,font=("Arial",18,"italic"),command=f5)
btnaddback=Button(addst,text="BACK",width=10,font=("Arial",18,"italic"),command=f2)

lblRno.pack(pady=5)
entRno.pack(pady=5)
lblName.pack(pady=5)
entName.pack(pady=5)
lblMarks.pack(pady=5)
entMarks.pack(pady=5)
btnaddsave.pack(pady=5)
btnaddback.pack(pady=5)

viewst=Toplevel(root)
viewst.title("View STUDENT")
viewst.geometry("400x300+300+200")
viewst.withdraw()
stData=scrolledtext.ScrolledText(viewst,width=40,height=10)
btnviewback=Button(viewst,text="BACK",width=10,font=("Arial",18,"italic"),command=f4)
stData.pack()
btnviewback.pack()


upst=Toplevel(root)
upst.title("UPDATE STUDENT")
upst.geometry("400x500+300+200")
upst.withdraw()
lblRno1=Label(upst,text="Enter Number",font=("Arial",18,"italic"))
entRno1=Entry(upst,bd=5,font=("Arial",18,"italic"))
lblMarks1=Label(upst,text="Enter Marks",font=("Arial",18,"italic"))
entMarks1=Entry(upst,bd=5,font=("Arial",18,"italic"))

btnaddsave1=Button(upst,text="SAVE",width=10,font=("Arial",18,"italic"),command=f12)
btnaddback1=Button(upst,text="BACK",width=10,font=("Arial",18,"italic"),command=f7)

lblRno1.pack(pady=5)
entRno1.pack(pady=5)
lblMarks1.pack(pady=5)
entMarks1.pack(pady=5)
btnaddsave1.pack(pady=5)
btnaddback1.pack(pady=5)



delst=Toplevel(root)
delst.title("DELETE STUDENT")
delst.geometry("400x500+300+200")
delst.withdraw()
lblRno2=Label(delst,text="Enter Number",font=("Arial",18,"italic"))
entRno2=Entry(delst,bd=5,font=("Arial",18,"italic"))
lblRno2.pack(pady=5)
entRno2.pack(pady=5)
btnaddsave2=Button(delst,text="SAVE",width=10,font=("Arial",18,"italic"),command=f13)
btnaddback2=Button(delst,text="BACK",width=10,font=("Arial",18,"italic"),command=f9)

lblRno2.pack(pady=5)
btnaddsave2.pack(pady=5)
btnaddback2.pack(pady=5)


grst=Toplevel(root)
grst.title("GRAPH")
grst.geometry("400x300+300+200")
grst.withdraw()
btnbar=Button(grst,text="BAR",width=10,font=("Arial",18,"italic"),command=f14)
btnline=Button(grst,text="LINE",width=10,font=("Arial",18,"italic"),command=f15)
btnpie=Button(grst,text="PIE",width=10,font=("Arial",18,"italic"),command=f16)
btnaddback3=Button(grst,text="BACK",width=10,font=("Arial",18,"italic"),command=f18)
btnbar.pack(pady=5)
btnline.pack(pady=5)
btnpie.pack(pady=5)
btnaddback3.pack(pady=5)



def quote():
	import requests
	import bs4
	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	soup=bs4.BeautifulSoup(res.text,'lxml')
	quote=soup.find('img',{"class":"p-qotd"})
	text=quote['alt']

	entqot.insert(0,text)
	
def temp():
	import socket
	import requests
	try:
		city='mumbai'
		
		socket.create_connection(("www.google.com",80))
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q=" + city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1 + a2 + a3
		res1=requests.get(api_address)
			
		data=res1.json()
	
		main=data['main']
	
		temp=main['temp']
		
		text2 = str(city) + ' ' + str(temp) + " "+"Celsius"
		enttemp.insert(0,text2)		

		
	except OSError:
		print("check network")
a = quote()
b = temp()


root.mainloop()