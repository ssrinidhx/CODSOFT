from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='darkgrey')
        master.resizable(False,False)
        
        self.equation=StringVar()
        self.entry_value=''
        Entry(width=25, bg='lightgrey', font=('Calibri', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.Show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.Show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.Show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.Show(1)).place(x=0, y=275)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda:self.Show(2)).place(x=90, y=275)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda:self.Show(3)).place(x=180, y=275)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda:self.Show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda:self.Show(4)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda:self.Show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda:self.Show(7)).place(x=0, y=125)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.Show(8)).place(x=90, y=125)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda:self.Show(9)).place(x=180, y=125)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda:self.Show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.Show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.Show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.Show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.Show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda:self.Show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.Solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', bg='lightgrey', command=self.Clear).place(x=0, y=350)
        
    def Show(self, value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def Clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def Solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

root=Tk()
calculator=Calculator(root)
root.mainloop()
