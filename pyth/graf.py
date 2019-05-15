from tkinter import *
root = Tk()
btk = Button(root, text='Кнопочка', width=10, height=2,
             bg='white', fg='black', font='Arial 14')
lab = Label(root, text='Your lastname:', font='Vivaldi 46')
Edit = Entry(root, width=20)
btk.pack()
lab.pack()
Edit.pack()
root.mainloop()