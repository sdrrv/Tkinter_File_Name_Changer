from tkinter import *
import os
from tkinter import filedialog
#--------------------------------------------------------------------------
prefix=""
direct=r""
#------------------------------------Functions------------------------------------
def select_prefix():
    global prefix
    try:
        prefix=entry_file.get()
        if not prefix:
            label_debug.config(text="Error", fg="Red")
        else:
            label_debug.config(text="Fix_Selected!", fg="Green")
    except:
        label_debug.config(text="Error", fg="Red")

def select_dir():
    global direct
    try:
        direct=filedialog.askdirectory()
        if not direct:
            label_debug.config(text="Error", fg="Red")
        else:
            label_debug.config(text="Dir_Selected!", fg="Green")
            label_Directory_selected.config(text=direct)
    except:
        label_debug.config(text="Error", fg="Red")


#-----------------------Creating--the--GUI---------------------------------
app=Tk()
app.title("File Name Changer")
app.geometry("650x200")
#----------------------------------Labels--------------------------------------

label_file=Label(app,text="File Prefix:",font=("Calibri",13), padx=10, pady=20)
label_file.grid(row=0,column=0)

label_Directory=Label(app,text="Directory:",font=("Calibri",13), padx=10, pady=20)
label_Directory.grid(row=1,column=0)

label_Directory_selected=Label(app,text="None Selected",font=("Bookman Old Style",10), fg="blue")
label_Directory_selected.grid(row=1,column=1)

label_debug=Label(app,text="",font=("Bookman Old Style",10), fg="Green")
label_debug.grid(row=3,column=2)
#--------------------------------------Entrys----------------------------------

entry_file=Entry(app,text="None", font=("Bookman Old Style",10))
entry_file.grid(row=0,column=1)

#------------------------------------Buttons-------------------------------------
button_select_prefix=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_prefix)
button_select_prefix.grid(row=0,column=2)

button_select_dir=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_dir)
button_select_dir.grid(row=1,column=2)

button_run=Button(app,text="Run", font=("Calibri",10), activebackground="green", relief="groove", fg="Red")
button_run.grid(row=2,column=1)
#---------------------------------Run----------------------------------------
app.mainloop()
#--------------------------------------------------------------------------