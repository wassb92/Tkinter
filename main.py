from tkinter import *
from fonctions import *
import csv


def cmd_quit():
    wn.destroy()

def cmd_connect():
    if (var_login.get() == "LeBoss" and var_pw.get() == "1234"):
        interface_connect.pack_forget()
        interface_manager.pack(pady=50)
    else:
        interface_connect.pack_forget()
        interface_saler.pack(pady=50)

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



# // ----- // CREATION DE LA FENETRE // ----- //
wn = Tk()
wn.title("GesMag")
wn.geometry("800x450")
wn.resizable(width=False, height=False)

bg = PhotoImage(file="back.png")
label_bg = Label(wn, image=bg)
label_bg.place(x=0, y=0)


# // ----- // INTERFACE DE CONNEXION // ----- //
# > --- creation des widgets --- <
interface_connect = Frame(wn)
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
interface_manager = Frame(wn)
btn_manager_add = Button(interface_manager, width=20, text="ajouter un cassier")
btn_manager_display = Button(interface_manager, width=20, text="afficher la liste des cassier")
btn_manager_delete = Button(interface_manager, width=20, text="supprimer un cassier")
btn_manager_follow = Button(interface_manager, width=20, text="suivi de vente")
btn_manager_saler_interface = Button(interface_manager, width=20, text="suivi de vente")
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