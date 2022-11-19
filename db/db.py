import sqlite3
def makedb():
    conn = sqlite3.connect("./db/database.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS warning(
            userid integer PRIMARY KEY,
            warns integer
            )""")
    c.execute("""CREATE TABLE IF NOT EXISTS discordlog(
            messageid integer PRIMARY KEY,
            userid integer,
            content TEXT
            )""")    
    conn.commit()
    conn.close()

def newuser(userid):
    conn = sqlite3.connect("./db/database.db")
    c=conn.cursor()
    c.execute("INSERT INTO warning VALUES (?,?)",(userid,0))
    conn.commit()
    conn.close()

def addwarn(userid):
    conn = sqlite3.connect("./db/database.db")
    c=conn.cursor()
    c.execute(f"SELECT warns FROM warning WHERE userid={userid}")
    warn=c.fetchone()
    newwarn=warn[0]+1
    c.execute(f"UPDATE warning SET warns={newwarn} WHERE userid={userid}")
    conn.commit()
    conn.close()
    return newwarn

def logging(userid,message):
    conn = sqlite3.connect("./db/database.db")
    c=conn.cursor()
    c.execute(f"SELECT messageid FROM discordlog")
    messageid=c.fetchall()
    try:
        int_messageid=int(messageid[len(messageid)-1][-1])
        if int_messageid!=16384:    
            int_messageid+=1
        else:
            int_messageid=0
    except:
        int_messageid=0
    c.execute(f"DELETE FROM discordlog WHERE messageid={int_messageid}")
    c.execute("INSERT INTO discordlog VALUES (?,?,?)",(int_messageid,userid,message))
    conn.commit()
    conn.close()