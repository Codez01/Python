import random
from tkinter import*
import explore

code = random.randint(100000,999999)
codestr = str(code)
top = Tk()
enter = Entry(top , width = 50 )

def helloCallBack():
   explore.Message("+972527099287" , "+12055484032" ,"Your Verification code is :")
   explore.Message("+972527099287", "+12055484032", code)
   top.destroy()

B = Button(top, text ="Send a verification code ! ",width=50,height=5, command = helloCallBack)

enter = Entry(top)



def checker():
    print(enter.get())
    print("lol")
B2 = Button(top, text ="check ",width=50,height=5, command = checker())

enter.pack()


B.pack()
B2.pack()

top.geometry('800x600')

top.mainloop()

enter =input("enter a number")

if(codestr ==enter):
    print("verified")
    verfied = True
else:
    print("not verified")
    verfied =False

if(verfied):
    print("hello welcome to the activated program version , congrats! ")
else:
    print("you need to be verified ,sorry !")

