from Tkinter import *
root=Tk()
root.title("About developer")
root.configure(bg="light pink")
def fun():
    root.destroy()
pc=Label(root,text="Name - Ronak sanghvi\n Batch - B6 \n E.Roll - 161B182\n Project Name-Quiz Quix ",font="times 20 bold")
pc.after(7000,fun)
pc.pack()
root.mainloop()
