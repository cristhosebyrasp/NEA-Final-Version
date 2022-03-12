
import sqlite3



import sqlite3

conn = sqlite3.connect ( 'dbases/track_metadata.db' )
c = conn.cursor()

from tkinter import *

top = Tk()
top.title('Search a soung')

# -----------------Right Frame Labels -------------------|
# at the moment can connect to the database but is not retrieving the data

search_soung = Entry()
search_soung.pack(side = LEFT, expand = True)

def get_soung():
    global title
    soung = search_soung.get()
    data = c.fetchall()
    print(data)
    for row in data:
        searchlist.append(row)
        var1=str(soung)
        read_from_db(var1)


def read_from_db(var):
    #curs.execute('SELECT * FROM songs WHERE TITLE = "Scream"(?)', ('%'+var+'%',))
    curs.execute('SELECT * FROM songs (?)', ('%'+var+'%',))


soung_name = ""
button = Button(top, text="Search a sound", command=get_soung)
button.pack()
text = Text()
text.insert( '1.0' , '''Search over a million sounds...''')

#--------------------------------------------------------|



mainloop()