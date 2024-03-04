import tkinter as tk

def mainwindow() :
    root = tk.Tk()
    root.title("Week7 : My Python GUI Application")
    root.geometry('700x700+400+30')
    root.option_add('*font','garamond 16')
    root.config(bg='pink')
    root.grid_rowconfigure((0,2),weight=1)
    root.grid_rowconfigure(1,weight=5)
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=5)
    return(root)

def layout() :
    #top side
    top.grid(row=0,column=0,columnspan=2,sticky='news')
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid_rowconfigure(0,weight=1)
    #bottom side
    bottom.grid_columnconfigure((0,1),weight=1)
    bottom.grid_rowconfigure(0,weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')
    #left side
    left.columnconfigure(0,weight=1)
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    left.grid(row=1,column=0,sticky="news")
    #right side
    right.columnconfigure((0,1),weight=1)
    right.rowconfigure((0,1,2),weight=1)
    right.grid(row=1,column=1,sticky="news")

def topside(top) :
    tk.Button(top,text= "Cake Menu",image=b1,compound="top",command=cakeclick).grid(row= 0,column=0,sticky="news")
    tk.Button(top,text= "Drink Menu",image=b2,compound="top",command=drinkclick).grid(row= 0,column=1,sticky="news")
    tk.Button(top,text= "Check out Menu",image=b3,compound="top",command=checkoutclick).grid(row= 0,column=2,sticky="news")

def bottomside(bottom) :
    tk.Button(bottom,text= "Reset Submit",command=resetclick).grid(row= 0,column=0,sticky="news")
    tk.Button(bottom,text= "Exit Program",image=b4,compound="left",command=quit).grid(row= 0,column=1,sticky="news")



def cakeclick() :
    checkoutframe.grid_forget()
    layout()
    pos = 0
    for i in range (len(menu1)) :
        tk.Label(left,bg="#B9F3FC",text=menu1[i]).grid(row=pos,ipadx=11)
        tk.Label(left,bg="#B9F3FC",image=cakes[i]).grid(row=pos+1,ipady=10)
        pos = pos +2
        tk.Label(right,bg="#AEE2FF",text="(Price : %d) Amount: "%(price1[i])).grid(row=i,column=0,sticky="e")
        tk.Spinbox(right,from_=0,to=100,width=10,justify="center",textvariable=amt1[i]).grid(row=i,column=1)

def drinkclick() :
    checkoutframe.grid_forget()
    layout()
    pos = 0
    for i in range (len(menu2)) :
        tk.Label(left,bg="#B9F3FC",text=menu2[i]).grid(row=pos)
        tk.Label(left,bg="#B9F3FC",image=drinks[i]).grid(row=pos+1)
        pos = pos +2
        tk.Label(right,bg="#AEE2FF",text="(Price : %d) Amount: "%(price2[i])).grid(row=i,column=0,sticky="e",ipadx=3)
        tk.Spinbox(right,from_=0,to=100,width=10,justify="center",textvariable=amt2[i]).grid(row=i,column=1)

def checkoutclick() :
    left.grid_forget()
    right.grid_forget()
    checkoutframe.columnconfigure(0,weight=1)
    checkoutframe.rowconfigure((0,3),weight=2)
    checkoutframe.rowconfigure((1,2),weight=1)
    checkoutframe.grid(row=1,columnspan=2,sticky="news")
    total1,total2 = 0,0
    for i in range(len(menu1)):
        total1 += amt1[i].get() * price1[i]
        total2 += amt2[i].get() * price2[i]
    tk.Label(checkoutframe,bg="#EBC7E6",text="~ Summary of Cake/Drink ~",fg="blue",font=("comic san ms",22,"bold")).grid(row=0)
    tk.Label(checkoutframe,bg="#EBC7E6",text="Total of your orders = %0.2f Baht"%(total1+total2),fg="blue",font=("comic san ms",22,"bold")).grid(row=3,sticky="n",ipadx=25)
    tk.Label(checkoutframe,bg="cyan",text="Total cake price : %0.2f Baht"%(total1)).grid(row=1,sticky="news")
    tk.Label(checkoutframe,bg="lightyellow",text="Total drink price : %0.2f Baht"%(total2)).grid(row=2,sticky="news")

    tk.Label(checkoutframe,bg="#EBC7E6",text="net = %0.2f Baht"%((total1+total2)*0.07),fg="blue",font=("comic san ms",22,"bold")).grid(row=6,sticky="n",ipadx=25)
    tk.Label(checkoutframe,bg="#EBC7E6",text="Total of your orders + net = %0.2f Baht"%((total1+total2)+(total1+total2)*0.07),fg="blue",font=("comic san ms",22,"bold")).grid(row=6,sticky="n",ipadx=25)
def resetclick() :
    for i in range(len(menu1)) :
        amt1[i].set(0)
        amt2[i].set(0)
    checkoutclick()
root = mainwindow()
#create top,left,right,bottom,checkout frame widgets
top = tk.Frame(root,bg='#7286D3')
left = tk.Frame(root,bg='#B9F3FC')
right = tk.Frame(root,bg='#AEE2FF')
bottom = tk.Frame(root,bg="#7286D3")
checkoutframe = tk.Frame(root,bg='#EBC7E6')
#define images for using in this program
img1 = tk.PhotoImage(file="w6img\drink1.png")
img2 = tk.PhotoImage(file="w6img\drink2.png")
img3 = tk.PhotoImage(file="w6img\drink2.png")
img4 = tk.PhotoImage(file="w6img\cake1.png")
img5 = tk.PhotoImage(file="w6img\cake1.png")
img6 = tk.PhotoImage(file="w6img\cake1.png")
b1 = tk.PhotoImage(file="w6img\drink1.png")
b2 = tk.PhotoImage(file="w6img\drink1.png")
b3 = tk.PhotoImage(file="w6img\drink1.png")
b4 = tk.PhotoImage(file="w6img\drink1.png")
drinks = [img1,img2,img3]
cakes = [img4,img5,img6]
menu1 = [' Strawberry Cake '," Cheese   Cake  ","Newyork Cheese Cake"]
menu2 = ['| Orange   Mixed |',' Lemonade Mixed ',"| Mojito  Miexd  Berry |"]
price1 = [145,120,130]
price2 = [120,100,90]
amt1 = [tk.IntVar() for x in menu1] #spy of cake
amt2 = [tk.IntVar() for x in menu2] #spy of drink
total = 0
discount = 0
net = 0
topside(top)
bottomside(bottom)
layout()
root.mainloop()