from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


f = ("Calibri", 14)

ws=()


if __name__ == "__main__":
    ws = Tk()
    frame=Frame(ws)
    ws.title('Music Suggestion Tool V.3 - Main')
    #ws.geometry ( '940x565' )
    ws.geometry ( '1000x600' )
    ws.config(bg='#92d050')

    main_frame = Frame(ws)

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

# -----------------Panel 1 ------------------|
main=()
login=()
panel1=()
panel2=()

def Home(self):
    self.destroy()
    import main

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

main=()
home_btn = tk.Button(
    top_frame,
    width=15,
    text='Home',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command= (main),
)



login2_btn = tk.Button(
    top_frame,
    width=15,
    text='Login',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    #command=login_response
    command=(login)
)

panel1_btn = tk.Button(
    top_frame,
    width=15,
    text='Panel',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=(panel1),

)

panel2_btn = tk.Button(
    top_frame,
    width=15,
    text='Panel 2',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=(panel2),
)

quit_btn = tk.Button(
    top_frame,
    width=15,
    text='Quit',
    font=f,
    bg='#92d050',
    fg='#000000',
    relief=FLAT,
    cursor='hand2',
    command=quit,
)
#-------------------------------------------------------|

cover = ImageTk.PhotoImage(Image.open("images/cover.png"))
imagelabel=Label(image=cover, pady=5, padx=5)
imagelabel.pack(side=BOTTOM)

#----------------widgets placement-----------------------|

home_btn.grid(row=0, column=0, pady=10, padx=20)
login2_btn.grid(row=0, column=1, pady=10, padx=20)
panel1_btn.grid(row=0, column=2, pady=10, padx=20)
panel2_btn.grid(row=0, column=3, pady=10, padx=20)
quit_btn.grid(row=0, column=4, pady=10, padx=20)
top_frame.place(x=5, y=0)
top_frame.pack()


left_frame.place(x=50, y=100)
left_frame.pack()


right_frame.place(x=500, y=100)
right_frame.pack()

ws.resizable(False, False)
#ws.resizable(True, True) # use that during development only
ws.mainloop()

