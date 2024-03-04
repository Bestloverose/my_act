#------------------------
# Author : Napat Phinitsap
# ID : 1660700475
# Section : 127D
# Date : January 16, 2024
# Lab Number : 2
from tkinter import *
def createwindow() :
    root = Tk()
    root.title("BasicGUI#1:Create main window")#ชื่อแอพ
    root.geometry('600x600')#ขนาดหน้าจอ
    root.configure(bg='#C0C0C0')
    return root
def createwidget(root):
    # Label col-0
    title1_lb = Label(root, fg='black', text='Registration Form', bg='#C0C0C0')
    title1_lb.grid(row=1, column=0, columnspan=2, pady=10, sticky='nsew')#sticky='nsew'หมายถึงให้มันติดกันทุกด้าน

    
    title1_lb = Label(root, text='Name:', bg='#C0C0C0')#กล่องข้อความname
    title1_lb.grid(row=4, column=0, padx=40, sticky="w")

    title1_lb = Label(root, text='Email:',bg='#C0C0C0')
    title1_lb.grid(row=5, column=0, padx=40, sticky="w")

    title1_lb = Label(root, text='Gender:', font='Tahoma 10', bg='#C0C0C0')
    title1_lb.grid(row=6, column=0, padx=40, sticky="w")

    title1_lb = Label(root, text='Phone Number:', font='Tahoma 10', bg='#C0C0C0')
    title1_lb.grid(row=9, column=0, padx=40,pady=5, sticky="w")

    title1_lb = Label(root, text='User Name:', font='Tahoma 10', bg='#C0C0C0')
    title1_lb.grid(row=10, column=0, padx=40,pady=5, sticky="w")

    title1_lb = Label(root, text='Password:', font='Tahoma 10', bg='#C0C0C0')
    title1_lb.grid(row=11, column=0, padx=40,pady=5, sticky="w")

    title1_lb = Label(root, text='Security Question:', font='Tahoma 10', bg='#C0C0C0')
    title1_lb.grid(row=12, column=0, padx=40,pady=5, sticky="w")

    title1_lb = Label(root, text='Answer:', font='Tahoma 10', bg='#C0C0C0')#BGหมายถึงbackgroud
    title1_lb.grid(row=13, column=0, padx=40,pady=5, sticky="w")
    # entry col-1
    box1 = Entry(root, bg='#EEFF00',width=30)#Entry ของname
    box1.grid(row=4, column=1,pady=5,padx=20,sticky="w")#grid ของEntry name
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=5, column=1,pady=5,padx=20,sticky="w")
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=9, column=1,pady=5,padx=20,sticky="w")
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=10, column=1,pady=5,padx=20,sticky="w")
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=11, column=1,pady=5,padx=20,sticky="w")
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=12, column=1,pady=5,padx=20,sticky="w")
    box1 = Entry(root, bg='#EEFF00',width=30)
    box1.grid(row=13, column=1,pady=5,padx=20,sticky="w")
    
    # radionbutton col -1
    up_rad_male = Radiobutton(root, text='Male', bg='#C0C0C0', value=1)
    up_rad_male.grid(row=6, column=1, sticky="w", padx=20)

    up_rad_female = Radiobutton(root, text='Female', bg='#C0C0C0', value=2)
    up_rad_female.grid(row=7, column=1, sticky="w", padx=20)

    up_rad_other = Radiobutton(root, text='Other', bg='#C0C0C0', value=3)
    up_rad_other.grid(row=8, column=1, sticky="w", padx=20)

    btn1 = Button(root, text='Cancel',width=15,height=2,bg='#00DEFC')
    btn1.grid(row=14, columnspan=2 ,sticky='w',padx=95)
    btn1 = Button(root, text='Register',width=15,height=2,bg='#00DEFC')
    btn1.grid(row=14, columnspan=3, sticky='w',padx=225,pady=20)
    testlb = Label(root,bg='#00DEFC')
    testlb.grid(row=4,column=4)

root = createwindow()
createwidget(root)
root.mainloop()