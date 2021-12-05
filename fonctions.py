from tkinter import *
import csv

def open_tk_stock(line):
    stock_wn = Tk()
    label_id = Label(stock_wn, text="ID:      "+line[1])
    label_nom = Label(stock_wn, text="article: "+line[2])
    label_nombre = Label(stock_wn, text="nombre:  "+line[3])
    label_prix = Label(stock_wn, text="prix:    "+line[4])
    label_id.pack(pady=5, padx=5)
    label_nom.pack(pady=5, padx=5)
    label_nombre.pack(pady=5, padx=5)
    label_prix.pack(pady=5, padx=5)
    stock_wn.mainloop()

def cmd_btn_stock_0():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[0])

def cmd_btn_stock_1():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[1])

def cmd_btn_stock_2():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[2])

def cmd_btn_stock_3():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[3])

def cmd_btn_stock_4():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[4])


def cmd_btn_stock_5():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[5])

def cmd_btn_stock_6():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[6])

def cmd_btn_stock_7():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[7])

def cmd_btn_stock_8():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[8])

def cmd_btn_stock_9():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[9])

def cmd_btn_stock_10():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[10])

def cmd_btn_stock_11():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[11])

def cmd_btn_stock_12():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[12])

def cmd_btn_stock_13():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[13])

def cmd_btn_stock_14():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[14])


def cmd_btn_stock_15():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[15])

def cmd_btn_stock_16():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[16])

def cmd_btn_stock_17():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[17])

def cmd_btn_stock_18():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[18])

def cmd_btn_stock_19():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[19])

def cmd_btn_stock_20():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[20])

def cmd_btn_stock_21():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[21])

def cmd_btn_stock_22():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[22])

def cmd_btn_stock_23():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[23])

def cmd_btn_stock_24():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[24])

def cmd_btn_stock_25():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[25])

def cmd_btn_stock_26():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[26])

def cmd_btn_stock_27():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[27])

def cmd_btn_stock_28():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[28])

def cmd_btn_stock_29():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[29])

def cmd_btn_stock_30():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[30])

def cmd_btn_stock_31():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[31])

def cmd_btn_stock_32():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[32])

def cmd_btn_stock_33():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[33])

def cmd_btn_stock_34():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[34])


def cmd_btn_stock_35():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[35])

def cmd_btn_stock_36():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[36])

def cmd_btn_stock_37():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[37])

def cmd_btn_stock_38():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[38])

def cmd_btn_stock_39():
    list_stock = []
    with open('.db/stock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            list_stock.append(line)
    open_tk_stock(list_stock[39])