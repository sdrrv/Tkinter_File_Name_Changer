from tkinter import *
import os
from tkinter import filedialog
#--------------------------------------------------------------------------
prefix=""
direct=r""
nome=""
ordem=97
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

def select_nome():
    global nome
    try:
        nome=entry_nome.get()
        if not nome:
            label_debug.config(text="Error", fg="Red")
        else:
            label_debug.config(text="Nome_Selected!", fg="Green")
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

def run():
    global ordem
    if not prefix:
        label_debug.config(text="Run_Error \n No Prefix", fg="Red")
    elif not direct:
        label_debug.config(text="Run_Error \n No Directory", fg="Red")
    elif not nome:
        label_debug.config(text="Run_Error \n No Nome", fg="Red")
    elif prefix and direct and nome:
        try:
            for file in os.listdir(direct):
                if prefix in file:
                    os.rename(direct+chr(92)+file,direct+chr(92)+nome+chr(ordem))
                    ordem+=1
        except:
            label_debug.config(text="Run_Error", fg="Red")
    else:
        label_debug.config(text="Run_Error", fg="Red")



#-----------------------Creating--the--GUI---------------------------------
app=Tk()
app.title("File Name Changer (Elvas)")
app.geometry("700x200")
#----------------------------------Labels--------------------------------------

label_file=Label(app,text="File Prefix:",font=("Calibri",13), padx=10, pady=20)
label_file.grid(row=0,column=0)

label_name_to_change=Label(app,text="Substituir por:",font=("Calibri",13), padx=10, pady=20)
label_name_to_change.grid(row=0,column=5)

label_Directory=Label(app,text="Directory:",font=("Calibri",13), padx=10, pady=20)
label_Directory.grid(row=1,column=0)

label_Directory_selected=Label(app,text="None Selected",font=("Bookman Old Style",10), fg="blue")
label_Directory_selected.grid(row=1,column=1)

label_debug=Label(app,text="",font=("Bookman Old Style",10), fg="Green")
label_debug.grid(row=3,column=2)
#--------------------------------------Entrys----------------------------------

entry_file=Entry(app, font=("Bookman Old Style",10))
entry_file.grid(row=0,column=1)

entry_nome=Entry(app, font=("Bookman Old Style",10))
entry_nome.grid(row=0,column=6)

#------------------------------------Buttons-------------------------------------
button_select_prefix=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_prefix)
button_select_prefix.grid(row=0,column=2)

button_select_nome=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_nome)
button_select_nome.grid(row=0,column=7)

button_select_dir=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_dir)
button_select_dir.grid(row=1,column=2)

button_run=Button(app,text="Run", font=("Calibri",10), activebackground="green", relief="groove", fg="Red", command=run)
button_run.grid(row=2,column=1)
#---------------------------------Run----------------------------------------
app.mainloop()
#--------------------------------------------------------------------------