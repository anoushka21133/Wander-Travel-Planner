import mysql.connector as sqlcon
import sys
from datetime import datetime

con1=sqlcon.connect(host="localhost",user="root",passwd="abc123",database="wander")
if con1.is_connected():
    print("connection established")
else:
    print("Error in connecting")
    sys.exit()
cursor1=con1.cursor()

def AddUser(username, name, city, dob, mail, pwd):
    global con1
    global cursor1

    s=""
    try:
        query1="select max(user_id) from user"
        cursor1.execute(query1)
        uid=cursor1.fetchone()
        uid2,=uid
        uid2=uid2+1
        
        query1="insert into user values(%s,%s,%s,%s,%s,%s,%s)"
        val=(uid2,username, name, city, dob, mail, pwd)
        res=cursor1.execute(query1,val)
    except sqlcon.Error as error :
        s="Error Adding User/User already exists"
        con1.rollback()
        
    con1.commit()
    return s

def PrintHistory():
    global con1
    global cursor1

    query1="select * from history"
    num=cursor1.execute(query1)
    results=cursor1.fetchall() 
    for row in results:
        print(row)
    print(cursor1.rowcount,"rows fetched ")

def FindUser(username,password):
    global con1
    global cursor1
    print(username,password)
    query1="select * from user where Username=%s and Password=%s"
    val=(username,password)
    cursor1.execute(query1,val)
    results=cursor1.fetchall()   
    if cursor1.rowcount==0:
        return 0
    else:
        print(results[0][0])
        return results[0][0]

def addHistory(userID,state):
    global con1
    global cursor1

    query= "INSERT INTO history(userID,state,Date_of_search) Values(%s,%s,%s)"
    data=(userID,state,datetime.now())
    cursor1.execute(query,data)
    con1.commit()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def getHistory(userID):
    global con1
    global cursor1
    
    query1="select * from history where userID=%s"
    data=(userID,)
    num=cursor1.execute(query1,data)
    results=cursor1.fetchall() 

    return results

def addtowishlist(userID,state):
    global con1
    global cursor1

    query= "insert into wishlist(userID,state,Date_of_search) Values(%s,%s,%s)"
    data=(userID,state,datetime.now())
    cursor1.execute(query,data)
    con1.commit()

def getWishlist(userID):
    global con1
    global cursor1
    
    query1="select * from wishlist where userID=%s"
    data=(userID,)
    num=cursor1.execute(query1,data)
    results=cursor1.fetchall() 

    return results

def sqlClose():
    global con1
    global cursor1

    cursor1.close()
    con1.close()



