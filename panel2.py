from tkinter import *
import tkinter as tk
from tkinter import Tk , Label , Entry , Button
import sqlite3
from tkinter.messagebox import showinfo , showerror

f = ("Calibri" , 14)

# ----------MainFrame---------|

if __name__ == "__main__":
    ws = Tk ()
    ws.title ( 'Music Suggestion Tool V.3 - Panel 2' )
    # ws.geometry ( '940x565' )
    ws.geometry ( '1000x800' )
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
    login_response = ()

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
        pady = 10 ,

    )

    right_frame.pack ()

# -----The track form------|
page1 = ()
page2 = ()
page3 = ()


def Home(self , master):
    home = Home ()
    import __main__


def Login(self):
    ws.destroy ()
    import page1


def Panel(self):
    ws.destroy ()
    import page2


def Panel2(self):
    ws.destroy ()
    import page3


# -----------------Top Frame Buttons --------------------|

home_btn = Button (
    top_frame ,
    width = 15 ,
    text = 'Home' ,
    font = f ,
    bg = '#92d050' ,
    fg = '#000000' ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = page1
)

login2_btn = Button (
    top_frame ,
    width = 15 ,
    text = 'Login' ,
    font = f ,
    bg = '#92d050' ,
    fg = '#000000' ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = login_response
)

panel_btn = Button (
    top_frame ,
    width = 15 ,
    text = 'Panel' ,
    font = f ,
    bg = '#92d050' ,
    fg = '#000000' ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = page2

)

panel2_btn = Button (
    top_frame ,
    width = 15 ,
    text = 'Panel 2' ,
    font = f ,
    bg = '#92d050' ,
    fg = '#000000' ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = page3
)

quit_btn = Button (
    top_frame ,
    width = 15 ,
    text = 'Quit' ,
    font = f ,
    bg = '#92d050' ,
    fg = '#000000' ,
    relief = FLAT ,
    cursor = 'hand2' ,
    command = ws.destroy
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

# ----------------------------------------------|


l1 = Label ( right_frame , text = "sound name" , bg = '#92d050' , font = (f , 36) )
# l1.pack ( side = TOP, fill=Y)
l1.pack ( anchor = NW )

l2 = Label ( right_frame ,
             text = 'Soung Artist - Album' ,
             bg = '#92d050' ,
             fg = '#000000' ,
             font = (f , 18) ,
             )
# l2.pack ( side = TOP, fill=Y)
l2.pack ( anchor = NW )

"""
Label (right_frame,
             text = 'Sound name',
             bg = '#92d050',
             fg = '#000000',
             font = (f , 18),
             ).grid(row=0, column=0, sticky=W, pady=10, padx=10)
             
Label (right_frame,
             text = 'Soung Artist - Album',
             bg = '#92d050',
             fg = '#000000',
             font = (f , 18),
             ).grid(row=0, column=0, sticky=W, pady=10, padx=10)
"""
# ------------------------------------------|

b1 = Button ( right_frame , text =
"""
BPM
"""
              , bg = '#0071c0' , font = f , relief = FLAT , width = 8 , height = 3 , highlightbackground = "black", highlightthickness = 2 ).pack (
    side = TOP , pady = 5 , padx = 10 , )


b2 = Button ( right_frame , text =
"""
Minor
"""
              , bg = '#0071c0' , font = f , relief = FLAT , width = 8 , height = 3 , highlightbackground = "black", highlightthickness = 2  ).pack (
    side = TOP , pady = 5 , padx = 10 )
b3 = Button ( right_frame , text =
"""
Genre
"""
              , bg = '#0071c0' , font = f , relief = FLAT , width = 8 , height = 3 , highlightbackground = "black", highlightthickness = 2  ).pack (
    side = TOP , pady = 5 , padx = 10 )

# ----------------Canva1-----------------------|

data = [21 , 20 , 19 , 16 , 14 , 13 , 11 , 9 , 4 , 3]


def prop(n):
    return 360.0 * n / 1000


c1 = tk.Canvas ( ws , width = 90 , height = 90 , bg = '#92d050' , relief = FLAT , highlightthickness = 0 )
c1.pack ( side = LEFT , pady = 20 , padx = 20 )
# c1.grid( row=3, column = 5, pady = 20 , padx = 20 )

c1.create_arc ( (2 , 2 , 90 , 90) , fill = "#FAF402" , outline = "#FAF402" , start = prop ( 0 ) ,
                extent = prop ( 200 ) )
c1.create_arc ( (2 , 2 , 90 , 90) , fill = "#2BFFF4" , outline = "#2BFFF4" , start = prop ( 200 ) ,
                extent = prop ( 400 ) )
c1.create_arc ( (2 , 2 , 90 , 90) , fill = "#E00022" , outline = "#E00022" , start = prop ( 600 ) ,
                extent = prop ( 50 ) )
c1.create_arc ( (2 , 2 , 90 , 90) , fill = "#7A0871" , outline = "#7A0871" , start = prop ( 650 ) ,
                extent = prop ( 200 ) )
c1.create_arc ( (2 , 2 , 90 , 90) , fill = "#294994" , outline = "#294994" , start = prop ( 850 ) ,
                extent = prop ( 150 ) )

# ----------------Canva2-----------------------|

data = [21 , 20 , 19 , 16 , 14 , 13 , 11 , 9 , 4 , 3]


def prop(n):
    return 360.0 * n / 1000


c2 = tk.Canvas ( right_frame , width = 90 , height = 90 , bg = '#92d050' , relief = FLAT , highlightthickness = 0 )
c2.pack ( side = LEFT , pady = 20 , padx = 20 )
# c2.grid( row=3, column = 6, pady = 20 , padx = 20 )

c2.create_arc ( (2 , 2 , 90 , 90) , fill = "#FAF402" , outline = "#FAF402" , start = prop ( 0 ) ,
                extent = prop ( 200 ) )
c2.create_arc ( (2 , 2 , 90 , 90) , fill = "#2BFFF4" , outline = "#2BFFF4" , start = prop ( 200 ) ,
                extent = prop ( 400 ) )
c2.create_arc ( (2 , 2 , 90 , 90) , fill = "#E00022" , outline = "#E00022" , start = prop ( 600 ) ,
                extent = prop ( 50 ) )
c2.create_arc ( (2 , 2 , 90 , 90) , fill = "#7A0871" , outline = "#7A0871" , start = prop ( 650 ) ,
                extent = prop ( 200 ) )
c2.create_arc ( (2 , 2 , 90 , 90) , fill = "#294994" , outline = "#294994" , start = prop ( 850 ) ,
                extent = prop ( 150 ) )

# ----------------Canva3-----------------------|


data = [21 , 20 , 19 , 16 , 14 , 13 , 11 , 9 , 4 , 3]


def prop(n):
    return 360.0 * n / 1000


c3 = tk.Canvas ( right_frame , width = 90 , height = 90 , bg = '#92d050' , relief = FLAT , highlightthickness = 0 )
c3.pack ( side = LEFT , pady = 20 , padx = 20 )
# c3.grid( row=3, column = 7, pady = 20 , padx = 20 )

c3.create_arc ( (2 , 2 , 90 , 90) , fill = "#FAF402" , outline = "#FAF402" , start = prop ( 0 ) ,
                extent = prop ( 200 ) )
c3.create_arc ( (2 , 2 , 90 , 90) , fill = "#2BFFF4" , outline = "#2BFFF4" , start = prop ( 200 ) ,
                extent = prop ( 400 ) )
c3.create_arc ( (2 , 2 , 90 , 90) , fill = "#E00022" , outline = "#E00022" , start = prop ( 600 ) ,
                extent = prop ( 50 ) )
c3.create_arc ( (2 , 2 , 90 , 90) , fill = "#7A0871" , outline = "#7A0871" , start = prop ( 650 ) ,
                extent = prop ( 200 ) )
c3.create_arc ( (2 , 2 , 90 , 90) , fill = "#294994" , outline = "#294994" , start = prop ( 850 ) ,
                extent = prop ( 150 ) )

# ----------------Canva4-----------------------|

data = [21 , 20 , 19 , 16 , 14 , 13 , 11 , 9 , 4 , 3]


def prop(n):
    return 360.0 * n / 1000


c4 = tk.Canvas ( right_frame , width = 90 , height = 90 , bg = '#92d050' , relief = FLAT , highlightthickness = 0 )
c4.pack ( side = LEFT , pady = 20 , padx = 20 )
# c4.grid( row=3, column = 8, pady = 20 , padx = 20 )

c4.create_arc ( (2 , 2 , 90 , 90) , fill = "#FAF402" , outline = "#FAF402" , start = prop ( 0 ) ,
                extent = prop ( 200 ) )
c4.create_arc ( (2 , 2 , 90 , 90) , fill = "#2BFFF4" , outline = "#2BFFF4" , start = prop ( 200 ) ,
                extent = prop ( 400 ) )
c4.create_arc ( (2 , 2 , 90 , 90) , fill = "#E00022" , outline = "#E00022" , start = prop ( 600 ) ,
                extent = prop ( 50 ) )
c4.create_arc ( (2 , 2 , 90 , 90) , fill = "#7A0871" , outline = "#7A0871" , start = prop ( 650 ) ,
                extent = prop ( 200 ) )
c4.create_arc ( (2 , 2 , 90 , 90) , fill = "#294994" , outline = "#294994" , start = prop ( 850 ) ,
                extent = prop ( 150 ) )

# --------------------------------------------------------|
text = Entry ( c1 , width = 15 , bg = '#92d050' , relief = FLAT )
text.insert ( 0 , "Energy" )
text.pack ( side = LEFT , padx = 10 , pady = 10 )

text = Entry ( c2 , width = 15 , bg = '#92d050' , relief = FLAT )
text.insert ( 0 , "Danceability" )
text.pack ( side = LEFT , padx = 10 , pady = 10 )

text = Entry ( c3 , width = 15 , bg = '#92d050' , relief = FLAT )
text.insert ( 0 , "Happiness" )
text.pack ( side = LEFT , padx = 10 , pady = 10 )

text = Entry ( c4 , width = 15 , bg = '#92d050' , relief = FLAT )
text.insert ( 0 , "Instrumentality" )
text.pack ( side = LEFT , padx = 10 , pady = 10 )

details_btn = Button ( right_frame , text = ' Details ... ' , bg = '#92d050' , font = f , fg = '#ffffff' ,
                       relief = RAISED ).pack (
    side = RIGHT )

l3 = Label ( right_frame ,
             text = 'More soungs like this: ' ,
             bg = '#92d050' ,
             fg = '#000000' ,
             font = (f , 18) ,
             highlightbackground = "black",
             highlightthickness = 2,
             )
l3.pack ( anchor = NW )


# --------------------------------------------------------|

def callback():
    print ( "click!" )


photo1 = tk.PhotoImage ( file = "images/orange.png" )
b1 = tk.Button ( right_frame , image = photo1 , bg='#b9e133', text = "0.99" , command = callback , pady = 5 , padx = 5 , height = 45 ,
                width = 250 , relief = FLAT, compound = tk.LEFT )
b1.place ( x = 1 , y = 300)

photo2 = tk.PhotoImage ( file = "images/grey.png" )
b2 = tk.Button ( right_frame , image = photo2 , bg='#b9e133', text = "0.97" , command = callback , pady = 5 , padx = 5 , height = 45 ,
                width = 250 , relief = FLAT, compound = tk.LEFT )
b2.place ( x = 300 , y = 300 )

photo3 = tk.PhotoImage ( file = "images/samon.png" )
b3 = tk.Button ( right_frame , image = photo3 , bg='#b9e133', text = "0.98" , command = callback , pady = 5 , padx = 5 , height = 45 ,
                width = 250 , relief = FLAT, compound = tk.LEFT )
b3.place ( x = 1 , y = 400 )

photo4 = tk.PhotoImage ( file = "images/blue.png" )
b4 = tk.Button ( right_frame , image = photo4 , bg='#b9e133', text = "0.96" , command = callback , pady = 5 , padx = 5 , height = 45 ,
                width = 250 , relief = FLAT, compound = tk.LEFT )
b4.place ( x = 300 , y = 400 )

# -------------------------------------------------------|

edit = Entry (right_frame)
edit.focus_set ()
find=()
butt = tk.Button (right_frame , text = 'Search again', command = find , pady = 1 , padx = 1 , height = 2 ,
                width = 20 , relief = FLAT, compound = tk.LEFT )
butt.pack(side=LEFT)


def find():

    text.tag_remove ('found' , '1.0' , END)
    s = edit.get ()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search ( s , idx , nocase = 1.0 ,
                                stopindex = END )
            if not idx: break
            lastidx = '%s+%dc' % (idx , len ( s ))
            text.tag_add ( 'found' )
        text.tag_config ( 'found' )
    edit.focus_set ()
butt.config(
    command = find
)


# ------------------widgets placement--------------------|

home_btn.grid ( row = 0 , column = 0 , pady = 10 , padx = 20 )
login2_btn.grid ( row = 0 , column = 1 , pady = 10 , padx = 20 )
panel_btn.grid ( row = 0 , column = 2 , pady = 10 , padx = 20 )
panel2_btn.grid ( row = 0 , column = 3 , pady = 10 , padx = 20 )
quit_btn.grid ( row = 0 , column = 4 , pady = 10 , padx = 20 )
top_frame.place ( x = 5 , y = 0 )

left_frame.place ( x = 50 , y = 100 )

right_frame.place ( x = 350 , y = 100,  )

ws.resizable ( True , True )  # use that during development only
ws.mainloop ()

if __name__ != '__main__':
    pass
else:
    main ()
