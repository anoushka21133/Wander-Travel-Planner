from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import plotly.graph_objects as go
from datetime import datetime

# Load data frame and tidy it.
import pandas as pd
import sys
sys.path.append('C:\paridhi\12th class!\Computer science\project class 12')
import sqluser_if as si

path="C:\\wander project\\"

window = Tk()

#global variables

userID=""
username=""
password=""
name=""
month=""
state=""
info=""
style = Style()


#function to clear screen
def clearScreen():
    list = window.pack_slaves()
    for l in list:
        l.destroy()

#functions called on button clicks
def loginClicked():
    clearScreen()
    LoginScreen()

def signupClicked():
    clearScreen()
    SignupScreen()
    

def userLoginClicked():
    global username
    global password
    global userID
    username=txt7.get()
    password=txt8.get()
    print(username,password)
    userID=si.FindUser(username,password)
    if password=="":
        showerror(title='input missing',message='Please enter password')
    if (userID==0):
        showerror(title='wrong input',message='Please check username/password')
    else:
        clearScreen()
        monthscreen()
        
def signClicked():
    Name=txt1.get()
    current_city=txt2.get()
    Date_of_birth=txt3.get()
    EmailID=txt4.get()
    username=txt5.get()
    password=txt6.get()
    s=si.AddUser(username,Name,current_city,Date_of_birth,EmailID,password)
    if s!="":
        showerror(title='Error',message=s)
    else:
        clearScreen()
        LoginScreen()
    

def detailClicked():
    global name
    global month
    
    #name=txt9.get()
    month=txt10.get()
    month=month.lower()
    if month=="":
        showerror(title='input missing',message='Please enter month')
    else :
        clearScreen()
        printScreen3()

def beginClicked():
    clearScreen()
    printScreen2()

def nextClicked():
    clearScreen()
    printScreen4()

def stateClicked():
    global state
    global userID
    
    state=txt3.get()
    state=state.capitalize()

    if state=="" :
         showerror(title='input missing',message='Please enter state')
    else:
        si.addHistory(userID,state)
        clearScreen()
        printScreen5()
        


def searchhistoryClicked():
    global userID
    
    results=si.getHistory(userID)
    
    popup = Tk()
    popup.wm_title("Search History")

    # create Treeview with 3 columns
    cols = ('Place', 'Date')
    listBox = Treeview(popup, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)
    
    # fill values
    for row in results:
        listBox.insert("", "end", values=(row[1],row[2]))

    popup.mainloop()

def addtowishlistClicked():
    global state
    global userID
    

    si.addtowishlist(userID,state)

    results=si.getWishlist(userID)
    
    popup = Tk()
    popup.wm_title("Wishlist")

    # create Treeview with 3 columns
    cols = ('Place', 'Date')
    listBox = Treeview(popup, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)
    
    # fill values
    for row in results:
        listBox.insert("", "end", values=(row[1],row[2]))

    popup.mainloop()


    

def lastClicked():
    clearScreen()
    printScreen6()

#functions for printing screens
def printScreen1():    
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                    font= 'Helvatica 24 bold', borderwidth=20,width= 24, anchor=CENTER,relief=RAISED)
    label = Label(top_frame, image = img).pack()
    btn = Button(bottom_frame, text = "Let the adventure begin..",style="BW.TLabel",command=beginClicked).pack(side = "bottom")


def printScreen2():
    label = Label(top_frame, image = img2).pack()
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="LOGIN",style="BW.TLabel", command=loginClicked).pack(side="bottom")
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="SIGN UP",style="BW.TLabel", command=signupClicked).pack(side="bottom")
    
    
##    # style configuration for button
##    style.configure("BW.TLabel", foreground="white", background="slate grey",
##                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
##    btn = Button(bottom_frame, text="Next..",style="BW.TLabel", command=detailClicked).pack(side="bottom")
def LoginScreen():
    label = Label(top_frame, image = img1).pack()
    lbl1 = Label(bottom_frame, text="hi",style="Label").pack()

    # style configuration for label
    style.configure("Label", font= 'Helvatica 10 bold')
    
    lbl1 = Label(bottom_frame, text="Enter username ",style="Label").pack()
    txt7.pack()
    lbl2 = Label(bottom_frame, text="Password ",style="Label").pack() 
    txt8.pack()
    
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="Next..",style="BW.TLabel", command=userLoginClicked).pack(side="bottom")

def SignupScreen():
    style.configure("Label", font= 'Helvatica 10 bold')
    
    lbl1 = Label(bottom_frame, text="Name ",style="Label").pack()
    txt1.pack()
    lbl2 = Label(bottom_frame, text="Current city ",style="Label").pack() 
    txt2.pack()
    lbl3 = Label(bottom_frame, text="Date of birth(YYYY-MM-DD) ",style="Label").pack() 
    txt3.pack()
    lbl4 = Label(bottom_frame, text="Email ID ",style="Label").pack() 
    txt4.pack()
    lbl5 = Label(bottom_frame, text="Enter username ",style="Label").pack() 
    txt5.pack()
    lbl6 = Label(bottom_frame, text="Password ",style="Label").pack() 
    txt6.pack()
    
    
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="Next..",style="BW.TLabel", command=signClicked).pack(side="bottom")

def monthscreen():
    label = Label(top_frame, image = img7).pack()
    # style configuration for label
    style.configure("Label", font= 'Helvatica 10 bold')

    #lbl9 = Label(bottom_frame, text="Please enter your name ",style="Label").pack()
    #txt9.pack()
    lbl10 = Label(bottom_frame, text="In which month do you want to travel ",style="Label").pack() 
    txt10.pack()
    
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="Next..",style="BW.TLabel", command=detailClicked).pack(side="bottom")



def printScreen3():
    label = Label(top_frame, image = img3).pack()
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="cyan4",
                font= 'Helvatica 12 bold', borderwidth=5,width= 40, anchor=CENTER,relief=RAISED)
    btn1 = Button(bottom_frame, text = "Temperature pattern..",style="BW.TLabel",command=plotTempMap).pack(side = "top")

    btn2 = Button(bottom_frame, text = "Precipitation pattern..",style="BW.TLabel",command=plotPptMap).pack(side = "top")
    
    btn3 = Button(bottom_frame, text = "Landform Distribution..",style="BW.TLabel",command=plotLandMap).pack(side = "top")    


    btn5 = Button(bottom_frame, text = "Next..",style="BW.TLabel",command=nextClicked).pack(side = "bottom")

  
def printScreen4():
    label = Label(top_frame, image = img4).pack()
    #global name

    # style configuration for label
    style.configure("Label", font= 'Helvatica 10 bold')    
    text1= "Enter name of state " 
    lbl1 = Label(bottom_frame, text=text1,style="Label").pack()
    
    txt3.pack()
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn1 = Button(bottom_frame, text="Next..",style="BW.TLabel", command=stateClicked).pack(side=BOTTOM)
    btn2 = Button(bottom_frame, text="Search History",style="BW.TLabel",command=searchhistoryClicked).pack(side=BOTTOM)

def printScreen5():
    label = Label(top_frame, image = img5).pack()
    global state
    global info
    
     # style configuration for label
    style.configure("Label", font= 'Helvatica 10 bold', space=4)
    consolinfo()
    lbl1 = Label(bottom_frame, text="Consolidated Information about "+state+"\n"+info, style="Label").pack()
    
    # style configuration for button
    style.configure("BW.TLabel", foreground="white", background="slate grey",
                font= 'Helvatica 12 bold', borderwidth=5,width= 10, anchor=CENTER,relief=RAISED)
    btn = Button(bottom_frame, text="Next..",style="BW.TLabel",command=lastClicked).pack(side=BOTTOM)
    btn2 = Button(bottom_frame, text="Add to Wishlist",style="BW.TLabel",command=addtowishlistClicked).pack(side=BOTTOM)
   
   
def printScreen6():
    label = Label(window, image = img6).pack()

#functions for plotting maps   
def plotTempMap():
        global month
        
        print("enter plotTempMap")
        df = pd.read_csv('US_monthly_temperature.csv')
        print("read file")
        
        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df[month], # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'thermal',
            colorbar_title = "Temperature(°F)",
            hoverinfo= "all",
            text=df['state']
        ))

        fig.update_layout(
            title_text = 'US temperature by State',
            geo_scope='usa', # limite map scope to USA
        )

        fig.show()

def plotPptMap():
        df = pd.read_csv('US_monthly_precipitation.csv')

        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df[month].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'teal',
            colorbar_title = "Precipitation",
            hoverinfo= "all",
            text=df['state']
        ))

        fig.update_layout(
            title_text = 'US precipitation by State',
            geo_scope='usa', # limite map scope to USA
        )

        fig.show()

def plotLandMap():
        df = pd.read_csv('US_landforms.csv')

        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df['tc'], # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'sunset',
            colorbar_title = "Landforms",
            hoverinfo= "all",
            text=df['Landform'],
            showscale=False
        ))

        fig.update_layout(
            title_text = 'US landforms by State',
            geo_scope='usa', # limite map scope to USA
        )

        fig.show()
                  

#function for fetching consolidated info for a state        
def consolinfo():
        global info
        df = pd.read_csv(path+'consolidated.csv')
        info="Landform type :" + df[state].values[0] + "\n" + "Annual high temperature :" + df[state].values[1] + "\n"+"Annual low temperature :"+df[state].values[2] + "\n"+"Annual precipitation :"+df[state].values[3] + "\n"+"Best place to visit :"+df[state].values[4] + "\n"

        
window.title("Welcome to WanderUSA")
window.geometry('620x680')
window.resizable(0, 0)

top_frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = "bottom")

# show image in top frame
img= PhotoImage(file = path+"\\pictures project\\wonder wander repeat.png")
img1 = PhotoImage(file = path+"\\pictures project\\img1.png")
img2 = PhotoImage(file = path+"\\pictures project\\img2.png")
img3 = PhotoImage(file = path+"\\pictures project\\img3.png")
img4 = PhotoImage(file = path+"\\pictures project\\img4.png")
img5 = PhotoImage(file = path+"\\pictures project\\img5.png")
img6 = PhotoImage(file = path+"\\pictures project\\img6.png")
img7 = PhotoImage(file = path+"\\pictures project\\img7.png")


txt1 = Entry(window,width=20,justify=CENTER)
txt2 = Entry(window,width=20,justify=CENTER)
txt3 = Entry(window,width=20,justify=CENTER)
txt4 = Entry(window,width=20,justify=CENTER)
txt5 = Entry(window,width=20,justify=CENTER)
txt6 = Entry(window,width=20,justify=CENTER)
txt7 = Entry(window,width=20,justify=CENTER)
txt8 = Entry(window,width=20,justify=CENTER)
txt9 = Entry(window,width=20,justify=CENTER)
txt10 = Entry(window,width=20,justify=CENTER)
printScreen1()

window.mainloop()
si.sqlClose()
