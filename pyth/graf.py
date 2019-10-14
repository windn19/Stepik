import Tkinter as tt

root = tt.Tk()
btk = tt.Button(root, text='Кнопочка', width=10, height=2,
             bg='white', fg='black', font='Arial 14')
lab = tt.Label(root, text='Your lastname:', font='Vivaldi 46')
Edit = tt.Entry(root, width=20)
btk.pack()
lab.pack()
Edit.pack()
root.mainloop()