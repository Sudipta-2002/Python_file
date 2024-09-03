from tkinter import *
#from tkinter import ttk
root = Tk()
Label(root,text="Name").grid(row=0)
Label(root,text="Roll").grid(row=1)
x1=Entry(root)
x2=Entry(root)
x1.grid(row=0,column=1)
x2.grid(row=1,column=1)

# Label(x1,text="sudipta").grid(row=0)
# Label(x2,text="166").grid(row=1)
mainloop()
