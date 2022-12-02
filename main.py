from rubika import Bot
import sqlite3,time
bot = Bot("tet","iiaijychaiythpkzalhlopejnbfogdxn")
con = sqlite3.connect('database.db')
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   phone TEXT,
   user_guid TEXT);
""")
con.commit()


def getData(phone):
	res = bot.addContact("F", "L", phone)
	return res

def getUserData(guid):
	pass
#----+--
'''
cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Nik', 'Piepenbreier', 'male');""")
conn.commit()

user = ('00002', 'Lois', 'Lane', 'Female')


cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()


print(bot.addContact("FirstName", "LastName", "09907742267"))

print( bot.getContacts()["data"]["users"][0]["phone"] )
'''
#989907742267

#""-"-"-"-"-"-""-"-"


z=0
start = 9360000000
end = 9369999999
try:
	for i in range(start,end):
		phoneN = str(z)+str(i)
		data = getData(phoneN)
		if data["user_exist"] == True:
			user_guid = data["user"]["user_guid"]
		
			c.execute("""INSERT INTO users(phone, user_guid) 
	   VALUES('{}','{}');""".format(phoneN,user_guid))
			con.commit()
			print(phoneN+" saved")
		else:
			print(phoneN+" no acc")
except:
	print(phoneN)
	open("lastphone.txt","w").write(phoneN)
	
	