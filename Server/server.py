from flask import Flask ,redirect,url_for,render_template,request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "anymistake",
        database = "database_project"
    )

cursor = db.cursor()

def addtolist(cur,a):
	for i in cur:
		a.append(i)



@app.route("/search")
a=[]
def search():
	name = request.args.get("name")
	query = f"select username,'user' as source from user where username like "%{name}%"" 
	cursor.execute(query)
	addtolist(cursor, a)
	query =f"select username,'listener' as source from listener where firstname like "%{name}%" or lastname like "%{name}%""
	cursor.execute(query)
	addtolist(cursor, a)
	query = f"select username,'artist' as source from artist where artisticname like "%{name}%""
	cursor.execute(query)
	addtolist(cursor, a)
	query = f"select title,'song' as source ,artist from song where title like "%{name}%""
	cursor.execute(query)
	addtolist(cursor, a)
	query = f"select title,'album' as source ,artist from album where title like "%{name}%""
	cursor.execute(query)
	addtolist(cursor, a)
	query = f"select title,'playlist' as source ,username from playlist where title like "%{name}%""
	cursor.execute(query)
	addtolist(cursor, a)
	




'''
@app.route("/login", methods=["POST"])
def login():
	username = 
	password =
	
	db.commit()
	return "Done!"
'''	