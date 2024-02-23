from tkinter import *
from tkinter.messagebox import*
from tkinter.font import *

def Check ():
    try:
        num= int(nt1.get())
        if num % 2 == 0:
            tx1.config(text=f'{num} is even.'
                       ' Thank you.')
        else:
            tx1.config(text=f'{num} is odd.'
                       ' Thank you.')
    except ValueError:
        tx1.config(text='Please Enter a valid number ! '
                   'Try Again.' ' Thank You.')

def reset():
    nt1.get()== END


win = Tk()
win.geometry('600x500')
win.title('Odd Or Even Printer')

lb1 = Label(win , text='Enter a number(0-10)',fg= 'blue', bg ='black')
lb1.place(width=500,height=50
          )

nt1= Entry(win, width=100 )
nt1.place(width=1000,height=50)

bt1 = Button(win , text= 'Check',border=3,command=Check)
bt1.grid(row=2,column=0)

bt2= Button(win , text='Reset' ,border= 3, command= reset  )
bt2.grid(row=2,column=1)

tx1 = Label(win, text='')
tx1.grid(row=3,column=0)

win.mainloop()