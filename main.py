from tkinter import *
from fonctions import *
from pathlib import Path
import tkinter.messagebox
import os
import csv

WINDOWS_SIZE = "1200x600"
MANAGER_ID = ""
MANAGER_PW = ""
DATA_DIR_PATH = "./.db"
SALER_DATA_PATH = "./.db/saler.csv"
SALER_CSV_HEADER = "id,name,firstname,birthday,address,zip,login,pw"

class Saler(object):
    def __init__(self, id, name, firstname, birthday, address, zip, login, pw):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.address = address
        self.zip = zip
        self.login = login
        self.pw = pw

saler = Saler("", "", "", "", "", "", "", "")

def cmd_quit():
    wn.destroy()

def is_account_in_database(login, password):
    fopn = open(SALER_DATA_PATH, "r")
    csv_file = csv.reader(fopn)
    login_id = 6
    login_pw = 7
    for row in csv_file:
        if login == row[login_id] and password == row[login_pw]:
            saler.id = row[0]
            saler.name = row[1]
            saler.firstname = row[2]
            saler.birthday = row[3]
            saler.address = row[4]
            saler.zip = row[5]
            saler.login = row[6]
            saler.pw = row[7]
            return True
    return False

def cmd_connect():
    login_failure = Label(interface_connect, text="Vous avez entré un nom d'utilisateur ou un mot de passe invalide", bg="red")
    if (var_login.get() == MANAGER_ID and var_pw.get() == MANAGER_PW):
        interface_connect.pack_forget()
        login_failure.pack_forget()
        interface_manager.pack(pady=50)
    elif (is_account_in_database(var_login.get(), var_pw.get())):
        interface_connect.pack_forget()
        login_failure.pack_forget()
        interface_saler.pack(pady=50)
    else:
        login_failure.pack()

def cmd_manager_disconnect():
    var_login.set("")
    var_pw.set("")
    interface_manager.pack_forget()
    interface_connect.pack(pady=70)

def cmd_saler_disconnect():
    var_login.set("")
    var_pw.set("")
    interface_saler.pack_forget()
    interface_connect.pack(pady=70)

def cmd_display_stock():
    interface_saler.pack_forget()
    interface_stock.pack(pady=50)

def cmd_stock_quit():
    interface_stock.pack_forget()
    interface_saler.pack(pady=50)

# Add saler
def cmd_add_saler():
    interface_manager.pack_forget()
    interface_add_saler.pack(pady=30)

def save_value_csv():
    path = Path(SALER_DATA_PATH)
    path_dir = Path(DATA_DIR_PATH)

    if not path_dir.exists():
        os.makedirs(DATA_DIR_PATH)
    if not path.is_file():
        f = open(SALER_DATA_PATH, 'x')
    f = open(SALER_DATA_PATH, 'a')
    data = csv.writer(f)

    saler_data = [add_saler_id.get(), add_saler_name.get(), add_saler_firstname.get(), add_saler_birthday.get(),
        add_saler_address.get(), add_saler_zip.get(), add_saler_login.get(), add_saler_pw.get()]

    data.writerow(saler_data)

    f.close()

def cmd_save_add_saler():
    onClick_successfull()
    save_value_csv()

def onClick_successfull():
    label_add_saler_successfull.pack()

def cmd_clean_add_saler():
    add_saler_id.set("")
    add_saler_name.set("")
    add_saler_firstname.set("")
    add_saler_birthday.set("")
    add_saler_address.set("")
    add_saler_zip.set("")
    add_saler_login.set("")
    add_saler_pw.set("")

def cmd_leave_quit_add_saler():
    interface_add_saler.pack_forget()
    label_add_saler_successfull.pack_forget()
    interface_manager.pack(pady=50)



# // ----- // CREATION DE LA FENETRE // ----- //
wn = Tk()
wn.title("GesMag")
wn.geometry(WINDOWS_SIZE)
wn.resizable(width=False, height=False)

bg = PhotoImage(file="main_background.png")
label_bg = Label(wn, image=bg)
label_bg.place(x=0, y=0)


# // ----- // INTERFACE DE CONNEXION // ----- //
# > --- creation des widgets --- <
interface_connect = Frame(wn)
interface_test = Frame(wn)
#login
var_login = StringVar()
frame_login = Frame(interface_connect)
label_login = Label(frame_login, text="login")
entry_login = Entry(frame_login, width=40, textvariable=var_login)
#pw
var_pw = StringVar()
frame_pw = Frame(interface_connect)
label_pw = Label(frame_pw, text="mot de passe")
entry_pw = Entry(frame_pw, width=40, show="*", textvariable=var_pw)
#boutons
frame_buttons = Frame(interface_connect)
btn_quit = Button(frame_buttons, text="quitter", command=cmd_quit, width=17)
btn_connect = Button(frame_buttons, text="connexion", command=cmd_connect, width=17)

# > --- placement des widgets --- <
label_login.pack()
entry_login.pack()
frame_login.pack(pady=5)
label_pw.pack()
entry_pw.pack()
frame_pw.pack(pady=5)
btn_quit.pack(side="left")
btn_connect.pack(side="right")
frame_buttons.pack(pady=5)
interface_connect.pack(pady=70)


# // ----- // INTERFACE MANAGER // ----- //
# > --- creation des widgets --- <
interface_manager = Frame(wn, bg="white")
btn_manager_add = Button(interface_manager, width=20, text="ajouter un cassier", command=cmd_add_saler)
btn_manager_display = Button(interface_manager, width=20, text="afficher la liste des cassier")
btn_manager_delete = Button(interface_manager, width=20, text="supprimer un cassier")
btn_manager_follow = Button(interface_manager, width=20, text="suivi de vente")
btn_manager_saler_interface = Button(interface_manager, width=20, text="interface de caissier")
btn_manager_disconnect = Button(interface_manager, width=20, text="deconexion", command=cmd_manager_disconnect)

# > --- placement des widgets --- <
btn_manager_disconnect.pack(pady=20)
btn_manager_add.pack(pady=5)
btn_manager_display.pack(pady=5)
btn_manager_display.pack(pady=5)
btn_manager_delete.pack(pady=5)
btn_manager_follow.pack(pady=5)
btn_manager_saler_interface.pack(pady=5)


# // ----- // INTERFACE CASSIER // ----- //
# > --- creation des widgets --- <
interface_saler = Frame(wn)
btn_saler_disconnect = Button(interface_saler, width=20, text="deconexion", command=cmd_saler_disconnect)
btn_saler_stock = Button(interface_saler, width=20, text="afficher le stock", command=cmd_display_stock)
btn_saler_ticket = Button(interface_saler, width=20, text="ticket de caisse")
btn_saler_export = Button(interface_saler, width=20, text="export statistique")

# > --- placement des widgets --- <
btn_saler_disconnect.pack(pady=20)
btn_saler_stock.pack(pady=5)
btn_saler_ticket.pack(pady=5)
btn_saler_export.pack(pady=5)

# > --- creation des widgets add saler --- <
interface_add_saler = Frame(wn, bg="white")
add_saler_id = StringVar()
add_saler_name = StringVar()
add_saler_firstname = StringVar()
add_saler_birthday = StringVar()
add_saler_address = StringVar()
add_saler_zip = StringVar()
add_saler_login = StringVar()
add_saler_pw = StringVar()

label_add_saler_id = Label(interface_add_saler, text="Identifiant (unique par caissier)", bg="white")
label_add_saler_name = Label(interface_add_saler, text="Nom", bg="white")
label_add_saler_firstname = Label(interface_add_saler, text="Prénom", bg="white")
label_add_saler_birthday = Label(interface_add_saler, text="Date de naissance (AAAA/MM/JJ)", bg="white")
label_add_saler_address = Label(interface_add_saler, text="Adresse", bg="white")
label_add_saler_zip = Label(interface_add_saler, text="Code postal", bg="white")
label_add_saler_login = Label(interface_add_saler, text="Login", bg="white")
label_add_saler_pw = Label(interface_add_saler, text="Mot de passe", bg="white")

label_add_saler_successfull = Label(interface_add_saler, text="Vos données ont bien été sauvegardés !", bg="green")

entry_add_saler_id = Entry(interface_add_saler, textvariable=add_saler_id, width=20)
entry_add_saler_name = Entry(interface_add_saler, textvariable=add_saler_name, width=20)
entry_add_saler_firstname = Entry(interface_add_saler, textvariable=add_saler_firstname, width=20)
entry_add_saler_birthday = Entry(interface_add_saler, textvariable=add_saler_birthday, width=20)
entry_add_saler_address = Entry(interface_add_saler, textvariable=add_saler_address, width=20)
entry_add_saler_zip = Entry(interface_add_saler, textvariable=add_saler_zip, width=20)
entry_add_saler_login = Entry(interface_add_saler, textvariable=add_saler_login, width=20)
entry_add_saler_pw = Entry(interface_add_saler, textvariable=add_saler_pw, width=20)

btn_add_saler_save = Button(interface_add_saler, text="Enregistrer", command=cmd_save_add_saler, width=17)
btn_add_saler_clean = Button(interface_add_saler, text="Vider", command=cmd_clean_add_saler, width=17)
btn_add_saler_quit = Button(interface_add_saler, text="Quitter", command=cmd_leave_quit_add_saler, width=17)


# > --- placement des widgets add_saler --- <
label_add_saler_id.pack()
entry_add_saler_id.pack()

label_add_saler_name.pack()
entry_add_saler_name.pack()

label_add_saler_firstname.pack()
entry_add_saler_firstname.pack()

label_add_saler_birthday.pack()
entry_add_saler_birthday.pack()

label_add_saler_address.pack()
entry_add_saler_address.pack()

label_add_saler_zip.pack()
entry_add_saler_zip.pack()

label_add_saler_login.pack()
entry_add_saler_login.pack()

label_add_saler_pw.pack()
entry_add_saler_pw.pack()

btn_add_saler_save.pack()
btn_add_saler_clean.pack()
btn_add_saler_quit.pack()


# // ----- // INTERFACE STOCK // ----- //
# > --- creation des widgets --- <
list_fonction = [
    cmd_btn_stock_0,
    cmd_btn_stock_1,
    cmd_btn_stock_2,
    cmd_btn_stock_3,
    cmd_btn_stock_4,
    cmd_btn_stock_5,
    cmd_btn_stock_6,
    cmd_btn_stock_7,
    cmd_btn_stock_8,
    cmd_btn_stock_9,
    cmd_btn_stock_10,
    cmd_btn_stock_11,
    cmd_btn_stock_12,
    cmd_btn_stock_13,
    cmd_btn_stock_14,
    cmd_btn_stock_15,
    cmd_btn_stock_16,
    cmd_btn_stock_17,
    cmd_btn_stock_18,
    cmd_btn_stock_19,
    cmd_btn_stock_20,
    cmd_btn_stock_21,
    cmd_btn_stock_22,
    cmd_btn_stock_23,
    cmd_btn_stock_24,
    cmd_btn_stock_25,
    cmd_btn_stock_26,
    cmd_btn_stock_27,
    cmd_btn_stock_28,
    cmd_btn_stock_29,
    cmd_btn_stock_30,
    cmd_btn_stock_31,
    cmd_btn_stock_32,
    cmd_btn_stock_33,
    cmd_btn_stock_34,
    cmd_btn_stock_35,
    cmd_btn_stock_36,
    cmd_btn_stock_37,
    cmd_btn_stock_38,
    cmd_btn_stock_39
]
interface_stock = Frame(wn)
frame_btns = Frame(interface_stock)
list_btn_stock = []
btn_stock_quit = Button(interface_stock, width=20, text="retour", command=cmd_stock_quit)
for x in range(10):
    for y in range(4):
        new_btn = Button(frame_btns, width=1, height=1, command=list_fonction[x+y*10])
        new_btn.grid(column=x, row=y)
        list_btn_stock.append(new_btn)

# > --- placement des widgets --- <
frame_btns.pack()
btn_stock_quit.pack(side="bottom")

wn.mainloop()