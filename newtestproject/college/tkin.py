
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Registration Form")

labl_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
labl_0.place(x=90, y=53)

labl_1 = Label(root, text="FullName", width=20, font=("bold", 10))
labl_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

labl_2 = Label(root, text="Email", width=20, font=("bold", 10))
labl_2.place(x=68, y=180)

entry_02 = Entry(root)
entry_02.place(x=240, y=180)

labl_3 = Label(root, text="Gender", width=20, font=("bold", 10))
labl_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5,  value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20,  value=2).place(x=290, y=230)

labl_4 = Label(root, text="Age:", width=20, font=("bold", 10))
labl_4.place(x=70, y=280)

entry_02 = Entry(root)
entry_02.place(x=240, y=280)
list_of_cntry=[ 'Enquiry' ,'Place' , 'Order' ,'Return']

cv = StringVar()
drplist = OptionMenu(root, cv, *list_of_cntry)
drplist.config(width=15)
cv.set('Select your purpose')
drplist.place(x=250, y=400)
def submit():
    messagebox.askyesno('confirm','Are you ready to confirm?')

Button(root, text='Submit', width=20, bg='brown', fg='white',command=submit).place(x=180, y=380)
Button(root, text='Logout', width=20, bg='brown', fg='white',command=submit).place(x=180, y=600)

# it will be used for displaying the registration form onto the window

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="department",menu=submenu)

menu1=Menu(submenu)
submenu.add_cascade(label="computer science",menu=menu1)
menu1.add_command(label="python")
menu1.add_command(label="java")

menu1.add_command(label="c++")
menu2=Menu(submenu)
submenu.add_cascade(label="commerce",menu=menu2)
menu2.add_command(label="bcom")
menu2.add_command(label="bba")
menu3=Menu(submenu)
submenu.add_cascade(label="humanities",menu=menu3)
menu3.add_command(label="social")

submenu.add_command(label="graphics")


root.mainloop()