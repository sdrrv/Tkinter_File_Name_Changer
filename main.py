from tkinter import *
import os
from tkinter import filedialog
import pickle
#--------------------------------------------------------------------------
prefix=""
direct=r""
nome=""
#------------------------------------Functions------------------------------------
def select_prefix():
    global prefix
    try:
        prefix=entry_file.get()
        if not prefix:
            label_debug_settings.config(text="Error", fg="Red")
        else:
            label_debug_settings.config(text=prefix, fg="Green")
            with open ('save.txt', 'wb') as f: 
                pickle.dump(prefix,f)
    except:
        label_debug_settings.config(text="Error", fg="Red")
        pass

def select_nome():
    global nome
    global entry_file
    try:
        if not entry_nome.get():
            label_debug.config(text="Error_Empty", fg="Red")
            return False
        else:
            nome2=int(entry_nome.get())
    except:
        label_debug.config(text="Error_NonNumeric", fg="Red")
        return False
    nome=entry_nome.get()
    try:
        if len(nome)!=10:
            label_debug.config(text="Error_!=10", fg="Red")
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
    ordem=97
    replace=[]
    if not prefix:
        label_debug.config(text="Run_Error \n No Prefix", fg="Red")
        new()
    elif not direct:
        label_debug.config(text="Run_Error \n No Directory", fg="Red")
    elif not nome:
        label_debug.config(text="Run_Error \n No Nome", fg="Red")
    elif prefix and direct and nome:
        try:
            for file in os.listdir(direct):
                if prefix in file:
                    replace.append(file)
            os.rename(direct+chr(92)+replace[0],direct+chr(92)+nome+".jpeg")
            replace.pop(0)
            for file in replace:
                os.rename(direct+chr(92)+file,direct+chr(92)+nome+chr(ordem)+".jpeg")
                ordem+=1
            label_debug.config(text="Finished!", fg="Green")
            
        except Exception as e:
            label_debug.config(text="Run_Error", fg="Red")
            print(e)
    else:
        label_debug.config(text="Run_Error", fg="Red")

def new():
    global label_debug_settings
    global entry_file
    new_app=Tk()
    new_app.title("Settings")
    new_app.geometry("400x100")

    label_file=Label(new_app,text="File Prefix:",font=("Calibri",13), padx=10, pady=20)
    label_file.grid(row=0,column=0)
    entry_file=Entry(new_app, font=("Bookman Old Style",10))
    entry_file.grid(row=0,column=1)

    button_select_prefix=Button(new_app,text="Select", font=("Calibri",10), activebackground="blue", relief="groove", command=select_prefix)
    button_select_prefix.grid(row=0,column=2)
    if not prefix:
        label_debug_settings=Label(new_app,text="No Selected",font=("Bookman Old Style",10), fg="Red")
    else:
        label_debug_settings=Label(new_app,text=prefix,font=("Bookman Old Style",10), fg="Green")
    label_debug_settings.grid(row=1,column=1)

    new_app.mainloop()
def load():
    global prefix
    try:
        with open ('save.txt', 'rb') as f:
            prefix=pickle.load(f)
    except:
        pass

def key(event):
    if len(event.char) == 1:
        run()
#-----------------------Creating--the--GUI---------------------------------
load()
app=Tk()
app.title("File Name Changer (Elvas)")
app.geometry("700x300")
#----------------------------------Labels--------------------------------------

label_name_to_change=Label(app,text="Substituir por:",font=("Calibri",13), padx=10, pady=20)
label_name_to_change.grid(row=0,column=0)

label_Directory=Label(app,text="Directory:",font=("Calibri",13), padx=10, pady=20)
label_Directory.grid(row=1,column=0)

label_Directory_selected=Label(app,text="None Selected",font=("Bookman Old Style",10), fg="blue")
label_Directory_selected.grid(row=1,column=1)

label_debug=Label(app,text="",font=("Bookman Old Style",10), fg="Green")
label_debug.grid(row=3,column=2)
#--------------------------------------Entrys----------------------------------

entry_nome=Entry(app, font=("Bookman Old Style",10))
entry_nome.grid(row=0,column=1)

#------------------------------------Buttons-------------------------------------

button_select_nome=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_nome)
button_select_nome.grid(row=0,column=3)

button_select_dir=Button(app,text="Select", font=("Calibri",10), activebackground="green", relief="groove", command=select_dir)
button_select_dir.grid(row=1,column=2)

button_run=Button(app,text="Run", font=("Calibri",10), activebackground="green", relief="groove", fg="Red", command=run)
button_run.grid(row=2,column=1)

button_test=Button(app,text="Settings", command=new)
button_test.grid(row=4,column=0)

#---------------------------------Run----------------------------------------
app.bind_all('<Key>', key)
app.mainloop()
#--------------------------------------------------------------------------