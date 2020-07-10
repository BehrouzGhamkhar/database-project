from flask import Flask ,redirect,url_for,render_template,request
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ghon",
        database = "dbproject"
    )

cursor = db.cursor()

def addtolist(cur,a):
	for i in cur:
		a.append(i)


a=[]
@app.route("/search")
def search():
	a = []
	name = request.args.get("name")
	query = "select username,'user' as source from user where username like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a)
	'''
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
	jsonObj = json.dumps(a)
	return jsonObj

if __name__ == "__main__":
	app.run(host ="localhost" , port =5000,debug=True)




'''
@app.route("/login", methods=["POST"])
def login():
	username = 
	password =
	
	db.commit()
	return "Done!"
'''	