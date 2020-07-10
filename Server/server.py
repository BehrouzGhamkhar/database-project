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

def addtolist(cur,result,queryType):
	for i in cur:
		if(queryType==1 or queryType==2 or queryType==3):
			mydict = {}
			mydict["name"] = i[0]
			mydict["type"] = i[1]
			result.append(mydict)
		elif(queryType==4 or queryType==5):
			mydict = {}
			mydict["name"] = i[0]
			mydict["type"] = i[1]
			mydict["artist"] = i[2]
			result.append(mydict)
		elif(queryType==6):
			mydict = {}
			mydict["name"] = i[0]
			mydict["type"] = i[1]
			mydict["owner"] = i[2]
			result.append(mydict)

a=[]
@app.route("/search")
def search():
	a = []
	name = request.args.get("name")
	query = "select username,'user' as source from user where username like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 1)
	query ="select username,'listener' as source from listener where firstname like '%" + str(name) +  "%' or lastname like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 2)
	query = "select username,'artist' as source from artist where artisticname like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 3)
	query = "select title,'song' as source ,artist from song where title like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 4)
	query = "select title,'album' as source ,artist from album where title like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 5)
	query = "select title,'playlist' as source ,username from playlist where title like '%" + str(name) +  "%'"
	cursor.execute(query)
	addtolist(cursor, a, 6)
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