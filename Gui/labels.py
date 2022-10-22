from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
global l
l=[]
option= [0,1,2,3,4,5]#create
opt=['☺','☻','♥','♦','♣','♠']




button_dict={}
def printt():
   for widget in win.winfo_children():widget.destroy()  
   for i in option:
      def func(x=i):
         return hi(x)
      button_dict[i]=ttk.Button(win, text=opt[i], command= func)
      print(opt[i-1])
      button_dict[i].pack()
printt()
def hi(a):
    l.append(a)
    print(l)
    if len(l)==2:
        opt[option.index(l[1])]+=opt[option.index(l[0])]
        l.clear()
        print(option)
    printt()
win.mainloop()