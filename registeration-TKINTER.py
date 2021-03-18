from tkinter import *



root = Tk()
root.title("Registeration Form")





enter = Entry(root , width = 50 ,borderwidth=5)
enter.insert(0 ,"Please enter your name here  ")

enter2 = Entry(root , width = 50 ,borderwidth=5)
enter2.insert(0 ,"Please enter your Job here  ")


enter3 = Entry(root , width = 50 ,borderwidth=5)
enter3.insert(0 ,"Please enter your Salary here  ")



enter.pack()
enter2.pack()
enter3.pack()


def click():
    label1= Label(root , text="your name is : " + enter.get() +"\n"+"your job is : " + enter2.get() +"\n"+ "your salary is :" + enter3.get())
    label1.pack()
button = Button(root ,text = "done", command=click)
button.pack()







root.mainloop()
