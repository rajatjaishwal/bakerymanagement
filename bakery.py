#bakery shop RAJAT JAISHWAL
from tkinter import *
from KEEpydb import KEEpydb
from tkinter import messagebox
from PIL import ImageTk,Image


class Main:
	def __init__(self,root):
		self.root=root
		self.db=KEEpydb.query('bakeryshop.database','rajatjaishwal','')
		self.buy()
		#self.loginscreen()
		
		#globalvars
		self.cart={}
	def drawline(self,where,width=1000,height=1,fg='black',x=0,y=0,):
		Frame(where,width=width,height=height,bg=fg).place(x=x,y=y)
	def loginscreen(self):
		frame=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(frame,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(frame,x=10,y=90,height=4,width=705)
		global username,password,label
		username,password=StringVar(),StringVar()
		
		Label(frame,text='Admin Login',fg='grey50',bg='white').place(x=20,y=110)
		username.set(' Username Here ..')
		password.set(' Password Here ..')
		e1=Entry(frame,textvariable=username)
		e1.place(x=20,y=180,width=700-20,height=50)
		e1.bind('<Button-1>',lambda e:username.set(''))
		e2=Entry(frame,textvariable=password)
		e2.place(x=20,y=215+20,width=700-20,height=50)
		e2.bind('<Button-1>',lambda e:password.set(''))
		label=Label(frame,text='',fg='red',bg='white')
		label.place(x=30,y=300)
		
		Button(frame,text='login',command=self.logincheck,bg='green',fg='white').place(x=20,y=350,width=700-20)
		Button(frame,text='Continue as Customer',command=self.customerHomeScreen).place(x=20,y=410,width=700-20)
	def logincheck(self):
		global username,password,label
		if str(self.db.search('username')[1])==str(username.get()):
			if str(int(self.db.search('password')[1]))==str(password.get()):
				self.adminHomeScreen()
			else:label.config(text='Password is Incorrect ...')
		else:label.config(text='Username is Incorrect ...')
	
	def customerHomeScreen(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		
		Label(f,text='Customer Mode',bg='white').place(x=20,y=110)
		Button(f,text='Buy Products',fg='white',bg='dodger blue',command=self.buy).place(x=100,y=200,width=520,height=70)
		Button(f,text='About Us !',fg='white',bg='dodger blue',command=self.AboutUs).place(x=100,y=200+75,width=520,height=70)
		Button(f,text='Exit',fg='white',bg='dodger blue',command=self.loginscreen).place(x=100,y=200+75+75,width=520,height=70)
	
	def AboutUs(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		
		Label(f,text='About Application',bg='white',fg='grey40',font='verdana 13').place(x=20,y=100)
		Label(f,bg='white',text='It is an application to provide a facility to buy products\nwithout wasting time in search of any item in Store.     ').place(x=20,y=150)
		Label(f,text='About Application Schema',bg='white',fg='grey40',font='verdana 13').place(x=20,y=250)
		Label(f,bg='white',text='• GUI [ TKINTER ]').place(x=60,y=300)
		Label(f,bg='white',text='• DATABASE [ KEEpydb v.0.6 ]').place(x=60,y=340)
		Label(f,text='Developer',bg='white',fg='grey40',font='verdana 13').place(x=20,y=400)
		Label(f,bg='white',text='• Head [ RAJAT JAISHWAL ]').place(x=60,y=450)
		Label(f,bg='white',text='• Database Designer [ RAKSHA KUSHWAHA ]').place(x=60,y=490)
		Button(f,text='Back',bg='red',fg='white',command=self.customerHomeScreen).place(x=10,y=800,width=700,height=70)
		
	def buy(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)	
		Label(f,text='Buy Products',bg='white',fg='grey40',font='verdana 13').place(x=20,y=100)
	
		Button(f,text='Make Payment',bg='forest green',fg='white',command=self.makePayment).place(x=10,y=1090,width=700,height=70)
		Button(f,text='Back',bg='red',fg='white',command=self.adminHomeScreen).place(x=10,y=1090+75,width=700,height=70)
		
		global shop,cart,activitybar
		shop=Listbox(f)
		shop.place(x=20,y=170,height=500,width=700-20)
		for i in range(6,int(self.db.get_cell('D1'))):
			#self.cart[str(int(self.db.get_cell('A'+str(i))))]=[str(self.db.get_cell('C'+str(i))),' > INR '+str(self.db.get_cell('E'+str(i)))]
			shop.insert(END,str(self.db.get_cell('C'+str(i)))+' > INR '+str(self.db.get_cell('E'+str(i))))
			
		#shop.bind('<curselection>',lambda e:cart.insert(END,'HII'))
		Label(f,text='Your Cart',bg='white',fg='grey40',font='verdana 10').place(x=20,y=680)
		cart=Listbox(f)
		cart.place(x=20,y=735,height=250,width=700-20)
		shop.bind('<<ListboxSelect>>',lambda e:self.updatecart())

		activitybar=Label(f,text='Activity > ',bg='white')
		activitybar.place(x=20,y=1000)
	
	def makePayment(self):
		global cart
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)	
		Label(f,text='Make Payment',bg='white',fg='grey40',font='verdana 13').place(x=20,y=100)
		
		items=cart.get(0,last=True)
		Label(f,text='MAKING BILL',fg='white',bg='forest green').place(x=20,y=175,width=700-20)
		#self.drawline(f,x=20,y=90,height=4,width=705)
		
		Label(f,text='ITEMS',fg='white',bg='grey50').place(x=20,y=175+38,width=404)
		Label(f,text='PRICE (INR)',fg='white',bg='cyan').place(x=20+403,y=175+38,width=700-403-20)
		itemname,price=Listbox(f,bg='grey50'),Listbox(f,bg='cyan')
		itemname.place(x=20,y=250,width=410,height=400)
		price.place(x=422,y=250,width=300-20,height=400)
		
		
		_total=0
		for i in items:
			j=i.split('>')
			itemname.insert(END,str(j[0]))
			price.insert(END,str(j[1]))
			_total=_total+int(str(j[1].split()[1]))
			itemname.see(END)
			price.see(END)
		
		Label(f,text='Grand Total :',fg='green',bg='white',font='verdana 15').place(x=20,y=670)
		Label(f,text='INR '+str(_total),fg='green',bg='white',font='verdana 15 bold').place(x=325,y=670)
		qr=ImageTk.PhotoImage(Image.open('bakeryshop.database/payment/upi/qr.jpg').resize((400,400), Image.ANTIALIAS))
		_qr=Label(f,image=qr,bg='white')
		_qr.image=qr
		_qr.place(x=260,y=750)
		Label(f,text='Scan Qr to',fg='black',bg='white',font='verdana 10').place(x=70,y=900)
		Label(f,text='Pay',fg='black',bg='white',font='verdana 14 bold').place(x=100,y=955)
		
		Button(f,text='Back',fg='white',bg='red',command=self.buy).place(x=20,y=1165,width=700-20,height=70)
		
	def updatecart(self):
		global shop,cart,activitybar
		try:
			cart.insert(END,str(shop.get(shop.curselection())))
			item=str(shop.get(shop.curselection())).split('>')[0]
			activitybar.config(text='Activity > '+item+' added in cart ..')
			cart.see(END)
			#_cart=str(shop.get(shop.curselection())).split()
			#self.cart=
			
		except Exception as e:
			cart.insert(END,str(e))
			cart.see(END)
			
	def adminHomeScreen(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		
		Label(f,text='Admin Panel : '+str(self.db.search('admin')[1]).upper(),bg='white').place(x=20,y=110)
		Button(f,text='View Products',fg='white',bg='dodger blue',command=self.ViewProducts).place(x=100,y=200,width=520,height=70)
		Button(f,text='Add Items',fg='white',bg='dodger blue',command=self.AddItems).place(x=100,y=200+75,width=520,height=70)
		Button(f,text='Logs',fg='white',bg='dodger blue').place(x=100,y=200+75+75,width=520,height=70)
		Button(f,text='Settings',fg='white',bg='dodger blue',command=self.settings).place(x=100,y=200+75+75+75,width=520,height=70)
		Button(f,text='Logout',fg='white',bg='dodger blue',command=self.loginscreen).place(x=100,y=200+75+75+75+75,width=520,height=70)
		
	def settings(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		Label(f,text='Settings',font='verdana 14',bg='white',fg='grey50').place(x=20,y=110)
		
		Button(f,text='Add Admin',fg='white',bg='dodger blue').place(x=100,y=200,width=520,height=70)
		Button(f,text='Billing Authority Name',fg='white',bg='dodger blue',command=self.AddItems).place(x=100,y=200+75,width=520,height=70)
		Button(f,text='Update Application',fg='white',bg='dodger blue').place(x=100,y=200+75+75,width=520,height=70)
		Button(f,text='Color Customisation',fg='white',bg='dodger blue',command=self.settings).place(x=100,y=200+75+75+75,width=520,height=70)
		Button(f,text='Back',fg='red',bg='white',command=self.loginscreen).place(x=100,y=200+75+75+75+75,width=520,height=70)
		
	def AddItems(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		Label(f,text='Add Items',font='verdana 14',bg='white').place(x=20,y=110)
		
		global product_name,product_category,product_price_perItem,product_quantity
		product_name=StringVar()
		product_category=StringVar()
		product_price_perItem=StringVar()
		product_quantity=StringVar()
		product_category.set(' Product Category Here ..')
		product_name.set(' Product Name Here ..')
		product_price_perItem.set(' Product Price Here ..')
		product_quantity.set(' Product Quantity Here ..')
		
		
		e1=Entry(f,textvariable=product_category)
		e2=Entry(f,textvariable=product_name)
		e3=Entry(f,textvariable=product_quantity)
		e4=Entry(f,textvariable=product_price_perItem)
		
		e1.place(x=20,y=200,width=700-40,height=60)
		e2.place(x=20,y=200+65,width=700-40,height=60)
		e3.place(x=20,y=200+65+65,width=700-40,height=60)
		e4.place(x=20,y=200+65+65+65,width=700-40,height=60)
		
		e1.bind('<Button-1>',lambda e:product_category.set(''))
		e2.bind('<Button-1>',lambda e:product_name.set(''))
		e3.bind('<Button-1>',lambda e:product_quantity.set(''))
		e4.bind('<Button-1>',lambda e:product_price_perItem.set(''))
		
		Button(f,text='Done',bg='forest green',fg='white',command=self.add).place(x=10,y=480,width=700,height=70)
		Button(f,text='Back',bg='red',fg='white',command=self.adminHomeScreen).place(x=10,y=480+75,width=700,height=70)
		

	def add(self):
			global product_name,product_category,product_price_perItem,product_quantity
			cell=int(self.db.get_cell('d1'))
			self.db.update('a'+str(cell),str(int(self.db.get_cell('d2')))) #update product ID
			self.db.update('b'+str(cell),str(product_category.get())) #product category
			self.db.update('c'+str(cell),str(product_name.get())) #product name
			self.db.update('d'+str(cell),str(product_quantity.get())) #product quantity
			self.db.update('e'+str(cell),str(product_price_perItem.get())) #product price per item
			self.db.update('d1',str(int(self.db.get_cell('d1'))+1))
			self.db.update('d2',str(int(self.db.get_cell('d2'))+1))
			self.db.save()
			
			messagebox.showinfo('StoreRoom',f'item : {product_name.get()}\nquantity : {product_quantity.get()} added Sucessfully ..')
			self.AddItems()
			
	def ViewProducts(self):
		f=Frame(self.root,bg='white').place(x=0,y=0,width=1000,height=1600)
		Label(f,text='Shree Ganesh Bakeries',font='verdana 15 bold',bg='white',fg='blue').place(x=20,y=20)
		self.drawline(f,x=10,y=90,height=4,width=705)
		Label(f,text='Items',font='verdana 14',bg='white',fg='grey50').place(x=20,y=110)
		l1=Listbox(font='verdana 10')
		l2=Listbox(font='verdana 10')
		l3=Listbox(font='verdana 10')
		l4=Listbox(font='verdana 10')
		
		Label(f,text='NAME                             CATEGORY        TOTAL      PRICE',bg='dodger blue',fg='white').place(x=20,y=175)
		
		l1.place(x=20,y=180+40,width=280,height=900-40)
		l2.place(x=295,y=180+40,width=200,height=900-40)
		l3.place(x=450,y=180+40,width=200,height=900-40)
		l4.place(x=600,y=180+40,width=100,height=900-40)
		
		for i in range(6,int(self.db.get_cell('D1'))):
			l1.insert(END,str(self.db.get_cell('C'+str(i))))
			l2.insert(END,str(self.db.get_cell('B'+str(i))))
			l3.insert(END,str(int(self.db.get_cell('D'+str(i)))))
			l4.insert(END,str(int(self.db.get_cell('E'+str(i)))))
		
		Button(f,text='Back',bg='red',fg='white',command=self.adminHomeScreen).place(x=10,y=1100,width=700,height=100)

if __name__=='__main__':
	r=Tk()
	Main(r)
	r.mainloop()