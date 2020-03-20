from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq
import random

con = sq.connect("/Users/ann_phan/NovelConsole.db")
c = con.cursor()

def get_Consumers():
    res = c.execute("SELECT * from Consumer")
    data = c.fetchall() 
    return data

def get_Writers():
    res = c.execute("SELECT * from Writer")
    data = c.fetchall() 
    return data

def get_Novels():
    res = c.execute("SELECT * from Novel")
    data = c.fetchall() 
    return data
	
def ConsumerBuysNovel():
    res = c.execute("SELECT ConsumerID, NovelID, Price WHERE ConsumerBuysNovel.ConsumerID = Consumer.ConsumerID and ConsumerBuysNovel.NovelID = Novel.NovelID")
    data = c.fetchall()
    return data

def add_novel(novelID, genre, title, price, publisher, writerID):
    ins_str = 'INSERT INTO Novel Values (' + str(novelID) + ', "' + str(genre) + '", "' + str(title) + '", ' + str(price) + ', "' + str(publisher) + '", ' + str(writerID) + ');'
    print(ins_str)
    res = c.execute(ins_str)
    con.commit()
   
def render_menu():
    window = Tk()
    window.title("Novel Main Menu")
    window.geometry("200x100")
    req = Button(window, text = "Choose an option", command = render_Novel_request)
    req.pack()

    rpt = Button(window, text = "Report results", command = render_Novel_report)
    rpt.pack()

    ext = Button(window, text = "Exit", command = lambda:end_program(window))
    ext.pack()
    window.mainloop()
     
def end_program(w):
    con.close()
    w.destroy()
    
def render_Novel_report():
    novels = get_Novels()
    tbl = ""
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += ", "
        tbl += "\n\n"
    messagebox.showinfo("Report results\n\n", tbl)


def render_Novel_request():

    nov_req_win = Tk()
    nov_req_win.title("Novel Request")
    nov_req_win.geometry("700x600")

    novelID = random.randint(1000000000,9999999999)

    gnr = tk.StringVar(nov_req_win)
    ttl = tk.StringVar(nov_req_win)
    prc = tk.StringVar(nov_req_win)
    pblr = tk.StringVar(nov_req_win)

    input_frame = Frame(nov_req_win)
    input_frame.pack(side = LEFT)
    
    lbl = Label(input_frame, text = "Choose a genre, title, price, publisher, writerID").pack()
    lblgenre = Label(input_frame, text = "Genre").pack()
    genre = Entry(input_frame, textvariable = gnr).pack()

    lbltitle = Label(input_frame, text = "Title").pack()
    title = Entry(input_frame, textvariable = ttl).pack()

    lblprice = Label(input_frame, text = "Price").pack()
    price = Entry(input_frame, textvariable = prc).pack()

    lblpublisher = Label(input_frame, text = "Publisher").pack()
    publisher = Entry(input_frame, textvariable = pblr).pack()

    option_frame = Frame(nov_req_win)
    option_frame.pack(side = RIGHT)

    writerID = get_Writers()
    writerIDlb = writerID_lb(nov_req_win, option_frame, writerID)

    rpt = Button(input_frame, text = "Enter Novel",
                 command = lambda: check_and_enter_selection(novelID, gnr.get(), ttl.get(), prc.get(), pblr.get(),
                            writerID[writerIDlb.curselection()[0]][0])).pack()
                
    
    nov_req_win.mainloop()

def check_and_enter_selection(novelID, genre, title, price, publisher, writerID):

    try:
        add_novel(novelID, genre, title, int(price), publisher, int(writerID))
        messagebox.showinfo("Success", "Your novel has been added")

    except:
        messagebox.showinfo("Error- Try again", "Possible errors:  \you chose an invalid writerID\nthe price is in an invalid format, \nsomeone else is entering a novel at the same time")
        return


def writerID_lb(w, f, writer):
    lblwriter = Label(f, text = "\n\nWriters\n").pack(side = TOP)

    sLb = Listbox(f, height = 8, width = 35, font = ("arial", 12), exportselection = False) 
    sLb.pack(side = BOTTOM, fill = Y)
                
    scroll = Scrollbar(w, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = sLb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    sLb.config(yscrollcommand = scroll.set)

    i = 0;
    for row in writer:
        sLb.insert(i, row)
        i += 1
    sLb.selection_set(first = 0)

    return sLb


render_menu()


