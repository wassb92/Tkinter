from tkinter import *
from fonctions import *
from datetime import datetime, timedelta
from time import gmtime, strftime
from pathlib import Path
import pandas as pd
import tkinter.messagebox
import os
import csv


WINDOWS_SIZE = "1600x800"
MANAGER_ID = "admin"
MANAGER_PW = "admin"
DATA_DIR_PATH = "./.db"
SALER_DATA_PATH = DATA_DIR_PATH + "/saler.csv"
STOCK_DATA_PATH = DATA_DIR_PATH + "/stock.csv"
TICKET_DATA_PATH = DATA_DIR_PATH + "/ticket.csv"
SALER_CSV_HEADER = "id,name,firstname,birthday,address,zip,login,pw"
STOCK_CSV_HEADER = "img,id,nom,n,prix"
TICKET_CSV_HEADER = "date,prix"

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

def import_stock():
    with open("./stock.txt",'r') as firstfile, open(STOCK_DATA_PATH,'w') as secondfile:
        for line in firstfile:
             secondfile.write(line)

def create_empty_database():
    path_dir = Path(DATA_DIR_PATH)
    path_saler = Path(SALER_DATA_PATH)
    path_stock = Path(STOCK_DATA_PATH)
    path_ticket = Path(TICKET_DATA_PATH)

    if not path_dir.exists():
        os.makedirs(DATA_DIR_PATH)
    if not path_saler.exists():
        f = open(SALER_DATA_PATH, 'x')
        header = csv.writer(f)
        header.writerow(SALER_CSV_HEADER.split(','))
        f.close()
    if not path_stock.exists():
        f = open(STOCK_DATA_PATH, 'x')
        header = csv.writer(f)
        import_stock()
        f.close()
    if not path_ticket.exists():
        f = open(TICKET_DATA_PATH, 'x')
        header = csv.writer(f)
        header.writerow(TICKET_CSV_HEADER.split(','))
        f.close()


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
    if (var_login.get() == MANAGER_ID and var_pw.get() == MANAGER_PW):
        interface_connect.pack_forget()
        interface_manager.pack(pady=50)
    elif (is_account_in_database(var_login.get(), var_pw.get())):
        interface_connect.pack_forget()
        interface_saler.pack(pady=50)
    else:
        tkinter.messagebox.showerror("Error !", "Vous avez entré un nom d'utilisateur ou un mot de passe invalide")

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

def cmd_stat_quit():
    interface_stat.pack_forget()
    interface_saler.pack(pady=50)

def cmd_ticket_quit():
    interface_ticket.pack_forget()
    interface_saler.pack(pady=50)

def delete_product(line, newPrice):
    df = pd.read_csv(STOCK_DATA_PATH)
    df.loc[line, 'n'] = newPrice
    df.to_csv(STOCK_DATA_PATH, index=False)

def cmd_add_article():
    global list_article
    index = 0
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            index = index + 1
            if (line[1] == article_id.get()):
                if (int(article_nb.get()) <= int(line[3])):
                    price = str(int(line[4]) * int(article_nb.get()))
                    new_line_text = line[2] + "(" + line[1] + ")" + " x" + article_nb.get() + " - " + price + "€"
                    new_line = Label(frame_ticket, text=new_line_text)
                    new_line.pack(side="top")
                    list_article.append(new_line)
                    total = ""
                    for i in range(ticket_total.get().__len__()-1):
                        total += ticket_total.get()[i]
                    ticket_total.set(str(int(total) + int(price))+"€")
                    total_article_left = int(line[3]) - int(entry_article_nb.get())
                    delete_product(index - 1, total_article_left)
                else:
                    tkinter.messagebox.showerror("Erreur !", "Il n'y a plus assez de stock")
    article_nb.set("")
    article_id.set("")

def cmd_validate_ticket():
    global list_article
    data_value = [ticket_date.get(), ticket_total.get()]
    file = open(".db/ticket.csv", "a")
    data = csv.writer(file)
    data.writerow(data_value)
    file.close()
    for line in list_article:
        line.pack_forget()
    list_article.clear()
    article_nb.set("")
    article_id.set("")
    ticket_total.set("0€")
    pass

def cmd_interface_ticket():
    global list_article
    for line in list_article:
        line.pack_forget()
    list_article.clear()
    article_nb.set("")
    article_id.set("")
    ticket_total.set("0€")
    date = strftime("%Y/%m/%d", gmtime())
    ticket_date.set(date)
    interface_saler.pack_forget()
    interface_ticket.pack(pady=50)

def day_exists(days, day):
    for item in days:
        a, b = item
        if (a == day):
            return True
    return False

def add_price_to_day(list_day, day, price):
    nb_day = 0
    for a_day in list_day:
        nb_day += 1
    for i in range(nb_day):
        a, b = list_day[i]
        if (a == day):
            total1 = ""
            for i in range(b.__len__()-1):
                total1 += b[i]
            total2 = ""
            for i in range(price.__len__()-1):
                total2 += price[i]
            b = str(int(total1) + int(total2)) + "€"
            list_day[i] = (a, b)

def cmd_interface_stat():
    with open(TICKET_DATA_PATH, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for line in csv_reader:
            if line[0] == "date" and line[1] == "prix":
                continue
            Label(interface_stat, text=line[0] + "   -   " + line[1]).pack()
    interface_saler.pack_forget()
    interface_stat.pack(pady=50)

# Add saler
def cmd_add_saler():
    interface_manager.pack_forget()
    interface_add_saler.pack(pady=30)

def save_value_csv():
    f = open(SALER_DATA_PATH, 'a')
    data = csv.writer(f)

    saler_data = [add_saler_id.get(), add_saler_name.get(), add_saler_firstname.get(), add_saler_birthday.get(),
        add_saler_address.get(), add_saler_zip.get(), add_saler_login.get(), add_saler_pw.get()]

    data.writerow(saler_data)
    f.close()

def error_add_saler():
    if (add_saler_login.get().__len__() == 0 or add_saler_address.get().__len__() == 0 or add_saler_birthday.get().__len__() == 0 or
        add_saler_firstname.get().__len__() == 0 or add_saler_id.get().__len__() == 0 or add_saler_zip.get().__len__() == 0 or
        add_saler_name.get().__len__() == 0 or add_saler_pw.get().__len__() == 0):
            tkinter.messagebox.showerror("Error !", "Tous les champs doivent être remplis")
            return (False)
    with open('.db/saler.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if (line[0] == add_saler_id.get()):
                tkinter.messagebox.showerror("Error !", "ID invalid: cet ID existe déjà")
                return (False)
    date = add_saler_birthday.get()
    if date.__len__() != 10:
        tkinter.messagebox.showerror("Error !", "Date de naissance invalide: format invalide (AAAA/MM/JJ) taille")
        return (False)
    for i in range(date.__len__()):
        if (i == 4 or i == 7):
            if (date[i] != '/'):
                tkinter.messagebox.showerror("Error !", "Date de naissance invalide: format invalide (AAAA/MM/JJ) slash")
                return (False)
        else:
            if (date[i] < '0' or date[i] > '9'):
                tkinter.messagebox.showerror("Error !", "Date de naissance invalide: format invalide (AAAA/MM/JJ) nb")
                return (False)
    code = add_saler_zip.get()
    if code.__len__() != 5:
        tkinter.messagebox.showerror("Error !", "code postal invalide (5 chiffres)")
        return (False)
    for i in range(code.__len__()):
        if (code[i] < '0' or code[i] > '9'):
            tkinter.messagebox.showerror("Error !", "code postal invalide (5 chiffres)")
            return (False)
    login = add_saler_login.get()
    for i in range(login.__len__()):
        if (login[i] < '0' or login[i] > '9') and (login[i] < 'A' or login[i] > 'Z') and (login[i] < 'a' or login[i] > 'z'):
            tkinter.messagebox.showerror("Error !", "login ivalide: le login ne doit contenir que des lettres et des chiffres")
            return (False)
    pw = add_saler_pw.get()
    maj = False
    min = False
    special = False
    if pw.__len__() < 8:
        tkinter.messagebox.showerror("Error !", "mot de passe invalide: un mot de passe de 8 caractères minimum dont 1 caractère spécial, une lettre majuscule et une lettre minuscule")
        return (False)
    for i in range(pw.__len__()):
        if (pw[i] >= 'a' and pw[i] <= 'z'):
            min = True
        elif (pw[i] >= 'A' and pw[i] <= 'Z'):
            maj = True
        else:
            special = True
    if (min == False or maj == False or special == False):
        tkinter.messagebox.showerror("Error !", "mot de passe invalide: un mot de passe de 8 caractères minimum dont 1 caractère spécial, une lettre majuscule et une lettre minuscule")
        return (False)
    return (True)

def cmd_save_add_saler():
    if (error_add_saler()):
        onClick_successfull()
        save_value_csv()

def onClick_successfull():
    tkinter.messagebox.showinfo("Succès", "Saisie avec succès")

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
    interface_manager.pack(pady=50)

# Display saler
def cmd_display_saler():
    interface_manager.pack_forget()
    interface_display_saler.pack(pady=30)

def find_saler_by_id():
    saler_list = []
    fopn = open(SALER_DATA_PATH, "r")
    csv_file = csv.reader(fopn)
    id = 0
    for row in csv_file:
        if display_saler_id.get() == row[id]:
            saler_list = row
    return saler_list

def cmd_display_saler_by_id():
    saler_list = find_saler_by_id()

    if (display_saler_id.get() == "" or saler_list == []):
        tkinter.messagebox.showerror("Erreur !", "L'identifiant n'existe pas")
        return
    Label(interface_display_saler, text="Identifiant : " + saler_list[0] + "\t Nom : " + saler_list[1] + "\t Prénom : " + saler_list[2] + "\t Date de naissance : "
        + saler_list[3] + "\t Adresse : " + saler_list[4] + "\t Code postal : " + saler_list[5] + "\t Login : " + saler_list[6] + "\t Mot de passe : " + saler_list[7], bg="white").pack()

    Label(interface_display_saler, text="________________________________________________________________", bg="white").pack()

def get_all_saler_datas():
    with open(SALER_DATA_PATH) as csvfile:
        data = list(csv.reader(csvfile))

    return data

def cmd_display_all_saler():
    data = get_all_saler_datas()

    with open(SALER_DATA_PATH) as csvfile:
        row_count = sum(1 for row in csvfile)

    for i in range(1, row_count):
        Label(interface_display_saler, text="Identifiant : " + data[i][0] + "\t Nom : " + data[i][1] + "\t Prénom : " + data[i][2] + "\t Date de naissance : "
            + data[i][3] + "\t Adresse : " + data[i][4] + "\t Code postal : " + data[i][5] + "\t Login : " + data[i][6] + "\t Mot de passe : " + data[i][7], bg="white").pack()
        Label(interface_display_saler, text="________________________________________________________________", bg="white").pack()


def cmd_clean_display_saler_id():
    display_saler_id.set("")

def cmd_quit_display_saler():
    cmd_clean_display_saler_id()
    interface_display_saler.pack_forget()
    interface_manager.pack(pady=50)

# delete saler
def cmd_delete_saler():
    interface_manager.pack_forget()
    interface_delete_saler.pack(pady=30)

def delete_row():
    new_saler_data = []
    data = get_all_saler_datas()
    id_exist = False
    with open(SALER_DATA_PATH) as csvfile:
        row_count = sum(1 for row in csvfile)
    for i in range(0, row_count):
        if data[i][0] != delete_saler_id.get():
            new_saler_data.append(data[i])
        else:
            id_exist = True
    if (id_exist):
        tkinter.messagebox.showinfo("Succès", "Suppression avec succès")
    else:
        tkinter.messagebox.showerror("Erreur !", "L'identifiant n'existe pas")
    return new_saler_data

def write_new_csv_saler():
    data_list = delete_row()
    file = open(SALER_DATA_PATH, "r+")
    data = csv.writer(file)
    lines_number= len(data_list)

    file.truncate(0)
    i = 0
    while i < lines_number and data_list[i]:
        data.writerow(data_list[i])
        i = i + 1
    file.close()

def cmd_delete_saler_by_id():
    write_new_csv_saler()


def cmd_clean_delete_saler_id():
    delete_saler_id.set("")

def cmd_quit_delete_saler():
    cmd_clean_delete_saler_id()
    interface_delete_saler.pack_forget()
    interface_manager.pack(pady=50)

# sales follow-up
def get_day_sales(day):
    total_sales = 0
    with open('.db/ticket.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if (line[0] == day):
                sales = ""
                for i in range(line[1].__len__()-1):
                    sales += line[1][i]
                total_sales += int(sales)
    return (total_sales)

def cmd_sales_follow_up():
    interface_manager.pack_forget()
    interface_sales_follow_up.pack(pady=20)
    histogram = []
    for i in range(7):
        date = str(datetime.today() - timedelta(days=i))
        day = ""
        for j in range(10):
            if (date[j] == "-"):
                day += "/"
            else:
                day += date[j]
        histogram.append((day, get_day_sales(day)))
    histogram.reverse()
    max = 0
    for histo in histogram:
        date, sales = histo
        if (sales > max):
            max = sales
    if not max:
        return
    for i in range(7):
        date, sales = histogram[i]
        var_histogram[i].set(str(sales) + "€")
        var_dates[i].set(date)
        height = ((sales * 10) / max) + 1
        label_histogram[i].config(height=int(height))

def cmd_quit_sales_follow_up():
    interface_sales_follow_up.pack_forget()
    interface_manager.pack()


# connect from manager to saler

def cmd_saler_connect():
    interface_manager.pack_forget()
    interface_saler.pack(pady=50)



# // ----- // CREATION DE LA FENETRE // ----- //
create_empty_database()
wn = Tk()
wn.title("GesMag")
wn.geometry(WINDOWS_SIZE)
wn.resizable(width=False, height=False)

bg = PhotoImage(file="assets/main_background.png")
label_bg = Label(wn, image=bg)
label_bg.place(x=0, y=0)


# // ----- // INTERFACE DE CONNEXION // ----- //
# > --- creation des widgets --- <
interface_connect = Frame(wn)
#login
var_login = StringVar()
frame_login = Frame(interface_connect)
label_login = Label(frame_login, text="Login")
entry_login = Entry(frame_login, width=40, textvariable=var_login)
#pw
var_pw = StringVar()
frame_pw = Frame(interface_connect)
label_pw = Label(frame_pw, text="Mot de passe")
entry_pw = Entry(frame_pw, width=40, show="*", textvariable=var_pw)
#boutons
frame_buttons = Frame(interface_connect)
btn_quit = Button(frame_buttons, text="Quitter", command=cmd_quit, width=17)
btn_connect = Button(frame_buttons, text="Connexion", command=cmd_connect, width=17)

# > --- placement des widgets --- <
label_login.pack()
entry_login.pack()
frame_login.pack(pady=5)
label_pw.pack()
entry_pw.pack()
frame_pw.pack(pady=5)
btn_quit.pack(side="right")
btn_connect.pack(side="left")
frame_buttons.pack(pady=5)
interface_connect.pack(pady=70)


# // ----- // INTERFACE MANAGER // ----- //
# > --- creation des widgets --- <
interface_manager = Frame(wn, bg="white")
btn_manager_add = Button(interface_manager, width=40, text="Ajouter un(e) cassier / cassière", command=cmd_add_saler)
btn_manager_display = Button(interface_manager, width=40, text="Afficher la liste des cassiers / cassières", command=cmd_display_saler)
btn_manager_delete = Button(interface_manager, width=40, text="Supprimer un cassiers / cassières", command=cmd_delete_saler)
btn_manager_follow = Button(interface_manager, width=40, text="Suivi de vente", command=cmd_sales_follow_up)
btn_manager_saler_interface = Button(interface_manager, width=40, text="Interface de cassiers / cassières", command=cmd_saler_connect)
btn_manager_disconnect = Button(interface_manager, width=40, text="Déconnexion", command=cmd_manager_disconnect)

# > --- placement des widgets --- <
btn_manager_add.pack(pady=8)
btn_manager_display.pack(pady=8)
btn_manager_delete.pack(pady=8)
btn_manager_follow.pack(pady=8)
btn_manager_saler_interface.pack(pady=8)
btn_manager_disconnect.pack(pady=8)


# // ----- // INTERFACE CAISSIER // ----- //
# > --- creation des widgets --- <
interface_saler = Frame(wn)
btn_saler_disconnect = Button(interface_saler, width=20, text="Déconnexion", command=cmd_saler_disconnect)
btn_saler_stock = Button(interface_saler, width=20, text="Afficher le stock", command=cmd_display_stock)
btn_saler_ticket = Button(interface_saler, width=20, text="Ticket de caisse", command=cmd_interface_ticket)
btn_saler_export = Button(interface_saler, width=20, text="Export statistique", command=cmd_interface_stat)

# > --- placement des widgets --- <
btn_saler_stock.pack(pady=5)
btn_saler_ticket.pack(pady=5)
btn_saler_export.pack(pady=5)
btn_saler_disconnect.pack(pady=20)

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

btn_add_saler_save.pack(pady=8)
btn_add_saler_clean.pack()
btn_add_saler_quit.pack()

# > --- creation des widgets display saler --- <
interface_display_saler = Frame(wn, bg="white")
display_saler_id = StringVar()

label_display_saler_id = Label(interface_display_saler, text="Identifiant", bg="white")

entry_display_saler_id = Entry(interface_display_saler, textvariable=display_saler_id, width=20)

btn_display_saler_by_id = Button(interface_display_saler, text="Afficher", width=17, command=cmd_display_saler_by_id)
btn_display_saler = Button(interface_display_saler, text="Afficher Tous", width=17, command=cmd_display_all_saler)
btn_display_saler_clean = Button(interface_display_saler, text="Vider", width=17, command=cmd_clean_display_saler_id)
btn_display_saler_quit = Button(interface_display_saler, text="Quitter", width=17, command=cmd_quit_display_saler)


# > --- placement des widgets display_saler --- <
label_display_saler_id.pack()
entry_display_saler_id.pack()

btn_display_saler_by_id.pack()
btn_display_saler.pack()
btn_display_saler_clean.pack()
btn_display_saler_quit.pack()




# > --- creation des widgets delete saler --- <
interface_delete_saler = Frame(wn, bg="white")
delete_saler_id = StringVar()

label_delete_saler_id = Label(interface_delete_saler, text="Identifiant", bg="white")

entry_delete_saler_id = Entry(interface_delete_saler, textvariable=delete_saler_id, width=20)

btn_delete_saler_by_id = Button(interface_delete_saler, text="Supprimer", width=17, command=cmd_delete_saler_by_id)
btn_delete_saler_clean = Button(interface_delete_saler, text="Vider", width=17, command=cmd_clean_delete_saler_id)
btn_delete_saler_quit = Button(interface_delete_saler, text="Quitter", width=17, command=cmd_quit_delete_saler)


# > --- placement des widgets delete_saler --- <
label_delete_saler_id.pack()
entry_delete_saler_id.pack()

btn_delete_saler_by_id.pack()
btn_delete_saler_clean.pack()
btn_delete_saler_quit.pack()



# > --- creation des widgets sales_follow_up --- <
label_histogram = []
var_histogram = []
for i in range(7):
    var_histogram.append(StringVar())
label_dates = []
var_dates = []
for i in range(7):
    var_dates.append(StringVar())
interface_sales_follow_up = Frame(wn, bg="white")
label_sales_follow_up = Label(interface_sales_follow_up, text="Suivi de vente", bg="white")
btn_delete_sales_follow_up = Button(interface_sales_follow_up, text="Quitter", width=17, command=cmd_quit_sales_follow_up)
frame_histogram = Frame(interface_sales_follow_up, bg="white")
frame_tab = []
for i in range(7):
    frame_tab.append(Frame(frame_histogram, bg="white", height=150, width=80))
    frame_tab[i].pack_propagate(False)
    label_histogram.append(Label(frame_tab[i], bg="light blue", width=10, height=1, textvariable=var_histogram[i]))
for i in range(7):
    label_dates.append(Label(frame_histogram, bg="white", width=10, height=1, textvariable=var_dates[i]))


# > --- placement des widgets sales_follow_up --- <
label_sales_follow_up.pack()
btn_delete_sales_follow_up.pack(side="bottom")
for i in range(7):
    frame_tab[i].grid(column=i, row=0, padx=1)
for i in range(7):
    label_histogram[i].pack(side="bottom")
for i in range(7):
    label_dates[i].grid(column=i, row=1, padx=1)
frame_histogram.pack(side="top", pady=5)


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

list_img = [
    "pomme",
    "poire",
    "annanas",
    "abricot",
    "concombre",
    "courgette",
    "mangue",
    "radis",
    "navet",
    "carotte",
    "baguette",
    "pain_au_chocolat",
    "croissant",
    "vienoise",
    "vienoise_au_chocolat",
    "pain_au_raisins",
    "muffin",
    "paris-brest",
    "éclair_au_chocolat",
    "éclair_au_café",
    "steak_haché",
    "steak",
    "saumon",
    "cabillo",
    "sole",
    "saucisse",
    "poulet",
    "bar",
    "riette",
    "caille",
    "balai",
    "balaillette",
    "pelle",
    "serviette",
    "detergent",
    "eponge",
    "gants",
    "torchon",
    "produit_à_vitre",
    "savon"
]


for i in range(len(list_img)):
    list_img[i] = PhotoImage(file="assets/"+list_img[i]+".png")

interface_stock = Frame(wn)
frame_btns = Frame(interface_stock)
list_btn_stock = []
btn_stock_quit = Button(interface_stock, width=20, text="retour", command=cmd_stock_quit)
for x in range(10):
    for y in range(4):
        new_btn = Button(frame_btns, command=list_fonction[x+y*10], image=list_img[x+y*10])
        new_btn.grid(column=x, row=y)
        list_btn_stock.append(new_btn)

# > --- placement des widgets --- <
frame_btns.pack()
btn_stock_quit.pack(side="bottom")

# // ----- // INTERFACE TICKET // ----- //
# > --- creation des widgets --- <
list_article = []
ticket_total = StringVar()
article_id = StringVar()
article_nb = StringVar()
ticket_date = StringVar()
interface_ticket = Frame(wn)
frame_article = Frame(interface_ticket)
frame_ticket = Frame(interface_ticket)
btn_ticket_quit = Button(interface_ticket, width=20, text="retour", command=cmd_ticket_quit)
label_atricle_id = Label(frame_article, text="id:")
label_atricle_nb = Label(frame_article, text="quantité:")
entry_article_id = Entry(frame_article, textvariable=article_id)
entry_article_nb = Entry(frame_article, textvariable=article_nb)
btn_article = Button(interface_ticket, text="ajouter article", width=20, command=cmd_add_article)
btn_ticket_validate = Button(interface_ticket, text="valider le ticket", width=20, command=cmd_validate_ticket)
label_ticket_date = Label(frame_ticket, textvariable=ticket_date)
label_ticket_total= Label(frame_ticket, textvariable=ticket_total)

# > --- placement des widgets --- <
btn_ticket_quit.pack(side="bottom", pady=8)
label_atricle_id.grid(column=0, row=0)
label_atricle_nb.grid(column=0, row=1)
entry_article_id.grid(column=1, row=0)
entry_article_nb.grid(column=1, row=1)
btn_ticket_validate.pack(side="bottom")
btn_article.pack(side="bottom")
frame_article.pack(side="bottom", pady=4)
label_ticket_date.pack(side="top")
label_ticket_total.pack(side="bottom")
frame_ticket.pack(side="top")


# // ----- // INTERFACE TICKET // ----- //
# > --- creation des widgets --- <
interface_stat = Frame(wn)
btn_stat_quit = Button(interface_stat, width=20, text="retour", command=cmd_stat_quit)

# > --- placement des widgets --- <
btn_stat_quit.pack(side="bottom", pady=8)

wn.mainloop()