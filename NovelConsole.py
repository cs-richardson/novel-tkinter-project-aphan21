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
    print("1. Enter Novel")
    print("2. Novel Report")
    print("3. Exit")
    choice = int(input("Choose an option:\t"))

    if choice == 1:
        render_Novel_request()
    elif choice == 2:
        render_Novel_report()
    elif choice == 3:
        end_program()
        return False;

    return True;

def end_program():
    con.close()

def render_Novel_report():
    novels = get_Novels()
    tbl = "|------------------------------------------------------------------\n|"
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += ", "
        tbl += "\n|"
    tbl += "-----------------------------------------------------------------"

    print("Report results\n\n" + tbl)

def render_Novel_request():
    novelID = random.randint(1000000000,9999999999)
    genre = input("enter genre:\t")
    title = input("enter title:\t")
    price = input("enter price:\t")
    publisher = input("enter publisher:\t")

    writerID = get_Writers()
    writerIDchoice = writerID_lb(writerID)

    check_and_enter_selection(novelID, genre, title, price, publisher, writerIDchoice)

def writerID_lb(writer):
    print("\n\nWriters\n")
    for row in writer:
        print(row)
    writerID = input("\nChoose a writer by ID num:\t")
    return writerID

def check_and_enter_selection(novelID, genre, title, price, publisher, writerID):

    try:
        #standard_input = novel(str(genre), str(title) , int(price), str(publisher), int(writerID))
        add_novel(novelID, genre, title, int(price), publisher, int(writerID))
        print("Success", "Your novel has been added")

    except:
        print("Error- Try again", "Possible errors:  \you chose an invalid writerID\nthe price is in an invalid format, \nsomeone else is entering a novel at the same time")

while(render_menu()):
    print("\n\nWelcome to our Novel Request system")

