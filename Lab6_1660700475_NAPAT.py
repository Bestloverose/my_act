from tkinter import *

def mainwindow() :
  root = Tk()
  
  x = root.winfo_screenwidth()/2 - (w/2)
  y = root.winfo_screenheight()/2 - (h/2)
  root.geometry("%dx%d+%d+%d"%(w,h,x,y))
  root.title("W6-Act created by Napat")
  root.option_add('*font','Garamond 16 ')
  menubar = Menu(root)
  # Windows OS
  menubar.add_command(label="Menu",command=menu) #การสร้างMenu add_comand
  menubar.add_command(label="Checkout",command=checkout)
  menubar.add_command(label="Exit",command=root.quit)
  
  root.config(bg="pink",menu=menubar)
  root.rowconfigure(0,weight=1)
  root.rowconfigure(1,weight=1)
  root.columnconfigure((0,1),weight=1)
  root.resizable(False, False)
  return root

def welcome() : #ฟังก์ชันwelcom
    heart = Label(root,image=hearti,fg='#9400D3', bg="pink",text="...Welcome to my resturant...",compound='top')
    heart.place(x=0,y=0,width=600,height=500)
    heart.grid(row=0,ipadx=0,ipady=110,columnspan=2,sticky='news')
    
def menu(): #ฟังก์ชันmenu
    frm1 = Frame(root,bg='#DCDCDC')
    frm1.place(x=0,y=0,width=600,height=500) #การวางเฟรม
    frm1.rowconfigure((0),weight=1)
    frm1.rowconfigure((1),weight=1)
    frm1.columnconfigure((0,1),weight=1)
  
    Label(frm1,text="Strawberry Cake :",font='Yeseva 14',fg='#66CCFF').grid(row=0,column=0,pady=20,sticky='n')
    Label(frm1,image=cake1,text="Price 85",font='Yeseva 14',compound='top',fg='navy', bg="#3366FF").grid(row=0,column=0,pady=50,sticky='n')
    qtycake1 = Spinbox(frm1,from_=0,to=10,font='Yeseva 14',fg='#CC00FF',width=5, justify='center',textvariable=cake1)
    qtycake1.grid(row=0,column=0,pady=80,ipadx=10,ipady=0,sticky='s')

    Label(frm1,text="Strawberry Mixed :",font='Yeseva 14',fg='#66CCFF').grid(row=0,column=1,pady=20,sticky='n')
    Label(frm1,image=drink1,text="Price 120",font='Yeseva 14',compound='top',fg='navy', bg="#3366FF").grid(row=0,column=1,pady=50,sticky='n')
    qtydrink1 = Spinbox(frm1,from_=0,to=10,font='Yeseva 14',fg='#CC00FF',width=5, justify='center',textvariable=drink1)
    qtydrink1.grid(row=0,column=1,pady=80,ipadx=10,ipady=0,sticky='s')
    
    Label(frm1,text="Cheese Cake :",font='Garamond 14',fg='#66CCFF').grid(row=0,column=0,pady=10,sticky='s')
    Label(frm1,image=cake2,text="Price 95",font='Yeseva 14',compound='top',fg='navy', bg="#3366FF").grid(row=1,column=0,sticky='n')
    qtycake2 = Spinbox(frm1,from_=0,to=10,font='Yeseva 14',fg='#CC00FF',width=5, justify='center',textvariable=cake2)
    qtycake2.grid(row=1,column=0,pady=30,ipadx=10,ipady=0,sticky='s')

    Label(frm1,text="Orange Mixed :",font='Yeseva 14',fg='#66CCFF').grid(row=0,column=1,pady=10,sticky='s')
    Label(frm1,image=drink2, bg="#3366FF").grid(row=1,column=1,sticky='n')
    Label(frm1,text='Price 140',font='Yeseva 14',compound='top',fg='navy', bg="#3366FF").grid(row=1,column=1,pady=60,sticky='s')
    qtydrink2 = Spinbox(frm1,from_=0,to=10,font='Yeseva 14',fg='#CC00FF',width=5, justify='center',textvariable=drink2)
    qtydrink2.grid(row=1,column=1,pady=30,ipadx=10,ipady=0,sticky='s')

    return(qtycake1,qtycake2,qtydrink1,qtydrink2)
  
def checkout() :
  frm2 = Frame(root,bg='#FFE4E1')
  frm2.place(x=0,y=0,width=600,height=500)
  frm2.rowconfigure((0,1,2,3,4,5),weight=1)
  frm2.columnconfigure((0,1,2,3),weight=1)

  for i in range(len(tittleList)) :
        Label(frm2,text=tittleList[i],fg='#4169E1',bg="#AFEEEE").grid(row=0,column=i)
        
  
  lb1 = Label(frm2,text='Strawberry Cake :',font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  lb1.grid(row=1,column=0,ipady=5,sticky='n')
  amt_cake1 = Label(frm2,bg="#AFEEEE")
  amt_cake1.grid(row=1,column=1,ipadx=5,ipady=0,sticky='n')
  pcake1 = Label(frm2,text="85",font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  pcake1.grid(row=1,column=2,ipadx=5,ipady=0,sticky='n')
  tcake1 = Label(frm2,bg="#AFEEEE")
  tcake1.grid(row=1,column=3,ipadx=5,ipady=0,sticky='n')
  
    
  lb2 = Label(frm2,text='Strawberry Mixed :',font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  lb2.grid(row=2,column=0,ipady=15,sticky='n')
  amt_cake2 = Label(frm2,bg="#AFEEEE")
  amt_cake2.grid(row=2,column=1,ipadx=5,ipady=0,sticky='n')
  pcake2 = Label(frm2,text="95",font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  pcake2.grid(row=2,column=2,ipadx=5,ipady=0,sticky='n')
  tcake2 = Label(frm2,bg="#AFEEEE")
  tcake2.grid(row=2,column=3,ipadx=5,ipady=0,sticky='n')
    
  lb3 = Label(frm2,text='Cheese Cake :',font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  lb3.grid(row=3,column=0,ipady=15,sticky='n')
  amt_drink1 = Label(frm2,bg="#AFEEEE")
  amt_drink1.grid(row=3,column=1,ipadx=5,ipady=0,sticky='n')
  pdrink1 = Label(frm2,text="120",font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  pdrink1.grid(row=3,column=2,ipadx=5,ipady=0,sticky='n')
  tdrink1 = Label(frm2,bg="#AFEEEE")
  tdrink1.grid(row=3,column=3,ipadx=5,ipady=0,sticky='n')
    
  lb4 = Label(frm2,text='Orange Mixed :',font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  lb4.grid(row=4,column=0,ipady=15,sticky='n')
  amt_drink2 = Label(frm2,bg="#AFEEEE")
  amt_drink2.grid(row=4,column=1,ipadx=5,ipady=0,sticky='n')
  pdrink2 = Label(frm2,text="140",font='Yeseva 14',fg='#4169E1',bg="#AFEEEE")
  pdrink2.grid(row=4,column=2,ipadx=5,ipady=0,sticky='n')
  tdrink2 = Label(frm2,font='Yeseva 14',bg="#AFEEEE")
  tdrink2.grid(row=4,column=3,ipadx=5,ipady=0,sticky='n')
  
  
  totalPice = Label(frm2,font='Yeseva 14')
  totalPice.grid(row=5,columnspan=4,ipadx=5,ipady=0,sticky='n')

  total = 0
  
  qty_cake1 = int(qtycake1.get())#การรับค่าจาก spinbox
  totalcake1 = qty_cake1 * 85  #เอาค่าของ spinbox * 85
  strcake1 = StringVar()
  strcake1.set("%0.2f"%totalcake1)#กำหนดค่าเริ่มต้นที่ ได้จาก totalcake1
  tcake1["text"] = strcake1.get()
  tcake1["bg"] = "lightblue"
  tcake1["fg"] = "navy"
  
  qty_cake11= StringVar()
  qty_cake11.set(qty_cake1)
  amt_cake1["text"]=qty_cake11.get()
  amt_cake1["bg"]="lightblue"
  amt_cake1["fg"]="navy"
    
  qty_cake2 = int(qtycake2.get())
  totalcake2 = qty_cake2 * 95
  strcake2 = StringVar()
  strcake2.set("%0.2f"%totalcake2)
  tcake2["text"] = strcake2.get()
  tcake2["bg"] = "lightblue"
  tcake2["fg"] = "navy"
  
  qty_cake22= StringVar()
  qty_cake22.set(qty_cake2)
  amt_cake2["text"]=qty_cake22.get()
  amt_cake2["bg"]="lightblue"
  amt_cake2["fg"]="navy"
   
  qty_drink1 = int(qtydrink1.get())
  totaldrink1 = qty_drink1 * 120
  strdrink1 = StringVar()
  strdrink1.set("%0.2f"%totaldrink1)
  tdrink1["text"] = strdrink1.get()
  tdrink1["bg"] = "lightblue"
  tdrink1["fg"] = "navy"
  
  qty_drink11= StringVar()
  qty_drink11.set(qty_drink1)
  amt_drink1["text"]=qty_drink11.get()
  amt_drink1["bg"]="lightblue"
  amt_drink1["fg"]="navy"
  
  qty_drink2 = int(qtydrink2.get())
  totaldrink2 = qty_drink2 * 140
  strdrink2 = StringVar()
  strdrink2.set("%0.2f"%totaldrink2)
  tdrink2["text"] = strdrink2.get()
  tdrink2["bg"] = "lightblue"
  tdrink2["fg"] = "navy"
  
  qty_drink22= StringVar()
  qty_drink22.set(qty_drink2)
  amt_drink2["text"]=qty_drink22.get()
  amt_drink2["bg"]="lightblue"
  amt_drink2["fg"]="navy"
    
  total = totalcake1 + totalcake2 + totaldrink1 + totaldrink2
  strtotal = StringVar()
  strtotal.set("Total Price = %0.2f Bahts"%total)
  totalPice["text"] = strtotal.get()
  totalPice["bg"] = "lightblue"
  totalPice["fg"] = "navy"
  
  return(amt_cake1,amt_cake2,amt_drink1,amt_drink2,tcake1,tcake2,tdrink1,tdrink2,totalPice)
  
w = 600 #กำหนดค่า width
h = 500 #กำหนดค่า high
root = mainwindow()

tittleList = ["Menu list","Amount","Prices","Total(Bahts)"] #list title ข้อความเพื่อเอาไปloop


hearti = PhotoImage(file="images/myshop.png").subsample(2,2)
cake1 = PhotoImage(file="images/cake1.png")
cake2 = PhotoImage(file="images/cake2.png")
drink1 = PhotoImage(file="images/drink1.png")
drink2 = PhotoImage(file="images/drink2.png")

qtycake1,qtycake2,qtydrink1,qtydrink2 = menu() #การรับค่าฟังก์ชัน
amt_cake1,amt_cake2,amt_drink1,amt_drink2,tcake1,tcake2,tdrink1,tdrink2,totalPice = checkout() #การรับค่าฟังก์ชัน

welcome()

root.mainloop()         