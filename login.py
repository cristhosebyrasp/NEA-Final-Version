from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3


f = ("Calibri", 14)

con = sqlite3.connect('dbases/userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    password text
                )
            ''')
con.commit()

#----------MainFrame---------|

if __name__ == "__main__":
    ws = Tk()
    ws.title('Music Suggestion Tool V.3 - page1')
    #ws.geometry ( '940x565' )
    ws.geometry ( '1000x600' )
    ws.config(bg='#92d050')



#-------ws-top_frame--------|

top_frame = Frame(
    ws,
    bd=0,
    bg='#92d050',
    relief=FLAT,
    padx=10,
    pady=10
)
top_frame.pack()

# ---------ws-right_frame-----------|
login_response=()

left_frame = Frame(
    ws,
    bd=2,
    bg='#000000',
    relief=FLAT,
    padx=10,
    pady=10
)
left_frame.pack()

#---------ws-right_frame-----------|

right_frame = Frame(
    ws,
    bd=2,
    bg="#92d050",
    relief=FLAT,
    padx=10,
    pady=10
)

right_frame.pack()


#-----------------Insert record------------------|

def insert_record():
    check_counter=0
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if  var.get() == "":
        warn = "Gender"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Select Country"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 8:
        try:
            con = sqlite3.connect('dbases/userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                'name': register_name.get(),
                'email': register_email.get(),
                'contact': register_mobile.get(),
                'gender': var.get(),
                'country': variable.get(),
                'password': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


def track_page():
    pass

#-----------------Login response------------------|

def login_response():
    global username, pwd
    try:
        con = sqlite3.connect('dbases/userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]

    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
        warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            #track_page()
            ws.destroy()
            import page2

        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)


var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[185])

register_country = OptionMenu(
    right_frame,
    variable,
    *countries)


# -----------------Panel 1 ------------------|


def sound_connection(db_file):

    conn = sqlite3.connect('dbases/track_metadata.db')
    cur = conn.cursor()

    #cur.execute('SELECT * FROM songs WHERE TITLE = "Scream"')
    songs = cur.fetchall()

    cur.execute('SELECT * FROM songs WHERE TITLE = "Scream"').fetchall()
    #print(rows)

    #print(connection.total_changes)
    print(songs[0])
    print(songs[0][1])

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


#-----------------Left Frame-------------------|

Label(
    left_frame,
    text="Enter Email",
    bg='#000000',
    fg='#FFFFFF',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Enter Password",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=1, column=0, pady=10)


Label(
    left_frame,
    text="Enter Password",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=2, column=0, pady=10)

Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=3, column=0, pady=10)
Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=4, column=0, pady=10)
Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=5, column=0, pady=10)
Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=6, column=0, pady=10)
Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=7, column=0, pady=10)
Label(
    left_frame,
    text="",
    bg='#000000',
    fg='#FFFFFF',
    font=f
).grid(row=8, column=0, pady=10)


email_tf = Entry(
    left_frame,
    font=f
)
pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
)
login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=FLAT,
    cursor='hand2',
    command=login_response
)

#-----------------Right Frame Labels -------------------|

Label(
    right_frame,
    text="Enter Name",
    bg="#92d050",
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Email",
    bg="#92d050",
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Contact Number",
    bg="#92d050",
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Gender",
    bg="#92d050",
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Country",
    bg="#92d050",
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg="#92d050",
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Re-Enter Password",
    bg="#92d050",
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg="#92d050",
    padx=10,
    pady=10,
)


register_name = Entry(
    right_frame,
    font=f
)

register_email = Entry(
    right_frame,
    font=f
)

register_mobile = Entry(
    right_frame,
    font=f
)


male_rb = Radiobutton(
    gender_frame,
    text='Male',
    bg="#92d050",
    variable=var,
    value='male',
    font=('Times', 10),

)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg="#92d050",
    variable=var,
    value='female',
    font=('Times', 10),

)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg="#92d050",
    variable=var,
    value='others',
    font=('Times', 10)

)

register_country = OptionMenu(
    right_frame,
    variable,
    *countries)

register_country.config(
    width=15,
    font=('Times', 12)
)
register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)


# widgets placement

home_btn.grid(row=0, column=0, pady=10, padx=20)
login2_btn.grid(row=0, column=1, pady=10, padx=20)
panel_btn.grid(row=0, column=2, pady=10, padx=20)
panel2_btn.grid(row=0, column=3, pady=10, padx=20)
quit_btn.grid(row=0, column=4, pady=10, padx=20)
top_frame.place(x=5, y=0)


email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=100)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=100)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=False, side=LEFT)
female_rb.pack(expand=False, side=LEFT)
others_rb.pack(expand=False, side=LEFT)

#ws.resizable(False, False)
ws.resizable(True, True) # use that during development only
ws.mainloop()

