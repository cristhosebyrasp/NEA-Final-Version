from tkinter import *
from tkinter import Tk , Label , Entry , Button
import sqlite3
from tkinter.messagebox import showinfo , showerror

f = ("Calibri" , 14)

# ----------MainFrame---------|

if __name__ == "__main__":
    ws = Tk ()
    ws.title ( 'Music Suggestion Tool V.3 - Panel 1' )
    #ws.geometry ( '940x565' )
    ws.geometry ( '1000x600' )
    ws.config ( bg = '#92d050' )

# -------ws-top_frame--------|

top_frame = Frame (
    ws ,
    bd = 0 ,
    bg = '#92d050' ,
    relief = FLAT ,
    padx = 10 ,
    pady = 10
)
top_frame.pack ()

# ---------ws-right_frame-----------|

left_frame = Frame (
    ws ,
    bd = 2 ,
    bg = '#000000' ,
    relief = FLAT ,
    padx = 10 ,
    pady = 10
)
left_frame.pack ()

# ---------ws-right_frame-----------|

right_frame = Frame (
    ws ,
    bd = 2 ,
    bg = "#92d050" ,
    relief = FLAT ,
    padx = 10 ,
    pady = 10
)

right_frame.pack ()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect( 'dbases/track_metadata.db')
    except Error as e:
        print("Con not connect to the track_metadata.db")
    return conn

def select_all_sounds(db_file):
    conn = sqlite3.connect ( 'dbases/track_metadata.db' )
    cur = conn.cursor ()
    cur.execute ( "SELECT * FROM sounds" )
    rows = cur.fetchall ()
    #cur.execute('SELECT * FROM songs WHERE TITLE = "Scream"')
    songs = cur.fetchall ()
    #cur.execute ( 'SELECT * FROM songs WHERE TITLE = "Scream"' ).fetchall ()
    #print(rows)
    for row in rows:
        print(row)


# -----The track form------|
page1=()
page2=()
page3=()

def Home(self, master):
    home=Home()
    import __main__


def Login(self):
    ws.destroy()
    import page1


def Panel(self):
    ws.destroy()
    import page2


def Panel2(self):
    ws.destroy()
    import page3

#-----------------Top Frame Buttons --------------------|

home_btn = Button(
    top_frame,
    width=15,
    text='Home',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=page1
)

login2_btn = Button(
    top_frame,
    width=15,
    text='Login',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=login_response
)

panel_btn = Button(
    top_frame,
    width=15,
    text='Panel',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=page2

)

panel2_btn = Button(
    top_frame,
    width=15,
    text='Panel 2',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=page3
)

quit_btn = Button(
    top_frame,
    width=15,
    text='Quit',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=ws.destroy
)

# -----------------Left Frame-------------------|


Label (
    left_frame ,
    text = 'Hello, <name> !' ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f

).grid ( row = 1 , column = 0 , pady = 10 )

Label (
    left_frame ,
    text = "Home" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 2 , column = 0 , pady = 10 )

Label (
    left_frame ,
    text = "Search" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 3 , column = 0 , pady = 10 )

Label (
    left_frame ,
    text = "Advanced Search" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 4 , column = 0 , pady = 10 )
Label (
    left_frame ,
    text = "" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 5 , column = 0 , pady = 10 )
Label (
    left_frame ,
    text = "" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 6 , column = 0 , pady = 10 )
Label (
    left_frame ,
    text = "" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 7 , column = 0 , pady = 10 )
Label (
    left_frame ,
    text = "" ,
    bg = '#000000' ,
    fg = '#FFFFFF' ,
    font = f
).grid ( row = 8 , column = 0 , pady = 10 )

email_tf = Entry (
    left_frame ,
    font = f
)
pwd_tf = Entry (
    left_frame ,
    font = f ,
    show = '*'
)
login_btn = Button (
    left_frame ,
    width = 15 ,
    text = 'Login' ,
    font = f ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = login_response
)

# -----------------Right Frame Labels -------------------|
# at the moment can connect to the database but is not retrieving the data

search_soung = Entry()
search_soung.pack(side = LEFT, expand = True)
text = Text()
text.insert(search_soung,  '1.0' , '''Search over a million sounds...''')

def get_soung():
    global soungs
    soungs = search_title.get()
    data = c.fetchall()
    print(title)
    for row in data:
        searchlist.append(row)
        var1=str(title)
        read_from_db(var1)


def read_from_db(var):
    #curs.execute('SELECT * FROM songs WHERE TITLE = "Scream"(?)', ('%'+var+'%',))
    curs.execute('SELECT * FROM songs (?)', ('%'+var+'%',))


soungs_title = ""
button = Button(top, text="Search a sound", command=get_title)
button.pack()

#--------------------------------------------------------|

text = Label(right_frame, text="Sound processing ...")
text.place(x=5,y=360)

# ------------------------------------------------------|

# widgets placement

home_btn.grid(row=0, column=0, pady=10, padx=20)
login2_btn.grid(row=0, column=1, pady=10, padx=20)
panel_btn.grid(row=0, column=2, pady=10, padx=20)
panel2_btn.grid(row=0, column=3, pady=10, padx=20)
quit_btn.grid(row=0, column=4, pady=10, padx=20)
top_frame.place ( x = 5 , y = 0 )

left_frame.place ( x = 50 , y = 100 )

right_frame.place ( x = 500 , y = 100 )

ws.resizable ( True , True )  # use that during development only
ws.mainloop ()
