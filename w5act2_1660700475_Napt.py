from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("GUI5: Class Activity of Week5")
    x = root.winfo_screenwidth()/2 - (w/2) #สามารถใช้ได้ตลอด
    y = root.winfo_screenheight()/2 - (h/2) #สามารถใช้ได้ตลอด
    root.geometry("%dx%d+%d+%d"%(w,h,x,y)) #สามารถใช้ได้ตลอด
    root.configure(bg='lightgreen')
    root.option_add("*font","Helvetica 10 bold")
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    return(root)

def createframe(root) :
    top = Frame(root,bg='#694E4E')
    left = Frame(root,bg='#F3C5C5')
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    left.columnconfigure((0,1),weight=1)
    right = Frame(root,bg='#886F6F')
    right.rowconfigure((0,1,2,3,4,5),weight=1)
    right.columnconfigure((0,1),weight=1)
    bottom = Frame(root,bg='#694E4E')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1),weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    left.grid(row=1,column=0,sticky='news')
    right.grid(row=1,column=1,sticky='news')
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(root,top,left,right,bottom)

def widgettop(top) : 
    Label(top,text="Little Dream House Cafe by [NAPAT]",fg='white',font=("Helvetica", "20"),bg="#694E4E",pady=10).pack()

def widgetleft(left) :
    for i in range(len(imgCakeList)):
        Label(left,image=imgCakeList[i]).grid(row=i)
    for i in range(len(cakeMenu)):
        Checkbutton(left, text=cakeMenu[i],variable=cakeVar[i],command=fnclick).grid(row=i,column=1,sticky='w',padx=20)
               
def widgetright(right) :   
    for i,item in enumerate(imgCoffList) :
        Label(right,image=item).grid(row=i)
    for i,item in enumerate(coffMenu) :
        Checkbutton(right,text=item,variable=coffeeVar[i],command=fnclick).grid(row=i,column=1,sticky='w',padx=20)
def widgetbottom(bottom) :
    showcake = Label(bottom,textvariable=cakespy,bg='#694E4E',font=("Helvetica", "10","bold"))
    showcake.grid(row=0,column=0,ipady=5,pady=5)
    showcoff = Label(bottom,textvariable=coffspy,bg='#694E4E',font=("Helvetica", "10","bold"))
    showcoff.grid(row=0,column=1,ipady=5,pady=5)
    return(showcake,showcoff)

def fnclick() :
    c1net = 0
    c2net = 0
    cakeprice = [125,110,140,100]
    coffprice = [80,70,100,90]
    
    for i in range(len(cakeMenu)):
        if cakeVar[i].get(): #ถ้าติ๊กจะทำงาน
            c1net = c1net + cakeprice[i]#เช็คbutton เมนู

        if coffeeVar[i].get():
            c2net = c2net + coffprice[i]

    showcake["bg"] = "#886F6F"
    showcake["fg"] = "yellow"
    cakespy.set("Cake Total Amount = %.2f Bahts."%c1net)
    #cake Total Amount = 365.00 Bahts.

    showcoff["bg"] = "#886F6F"
    showcoff["fg"] = "yellow"
    coffspy.set("Coffee Total Amount = %.2f Bahts."%c2net)
    # Coffee Total Amount = 170.00 Bahts.

w = 650
h = 500
root = mainwindow()

cake1 = PhotoImage(file='image/cake1.png')
cake2 = PhotoImage(file='image/cake2.png')
cake3 = PhotoImage(file="image/cake3.png")
cake4 = PhotoImage(file="image/cake4.png")
coffee1 = PhotoImage(file="image/coffee1.png")
coffee2 = PhotoImage(file="image/coffee2.png")
coffee3 = PhotoImage(file="image/coffee3.png")
coffee4 = PhotoImage(file="image/coffee4.png")

cakeMenu = ["Stawberry Cake\n125 B.","Cheese Cake\n110 B.","Babybloom Cake\n140 B.","Chocolate Cake\n100 B."]
coffMenu = ["Hot Latte\n80 B.","Hot Cappuccino\n70 B.","Hot Caramel Latte\n100 B."," Hot Chocolate\n90 B."]

cakeVar = [IntVar() for i in cakeMenu]           #
coffeeVar = [IntVar() for i in coffMenu]         #

imgCakeList = [cake1,cake2,cake3,cake4]          #
imgCoffList = [coffee1,coffee2,coffee3,coffee4]  #

root,top,left,right,bottom = createframe(root)
widgettop(top)
widgetleft(left)                                 #
widgetright(right)                               #
cakespy,coffspy = StringVar(),StringVar()
showcake,showcoff = widgetbottom(bottom)
root.mainloop()