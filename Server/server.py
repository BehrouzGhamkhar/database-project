from flask import Flask ,redirect,url_for,render_template,request
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "anymistake",
        database = "database_project"
    )

cursor = db.cursor()

def addtolist1(cur,result,queryType):
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


@app.route("/search")
def search():
	a = []
	name = request.args.get("name")
	query = "select username,'user' as source from user where username like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 1)
	query ="select username,'listener' as source from listener where firstname like '%" + str(name) +  "%' or lastname like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 2)
	query = "select username,'artist' as source from artist where artisticname like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 3)
	query = "select title,'song' as source ,artist from song where title like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 4)
	query = "select title,'album' as source ,artist from album where title like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 5)
	query = "select title,'playlist' as source ,username from playlist where title like '%" + str(name) +  "%';"
	cursor.execute(query)
	addtolist1(cursor, a, 6)
	jsonObj = json.dumps(a)
	return jsonObj


'''
@app.route("/view")
def view():
	a=[]
	usrname = request.args.get("usrname")
	query = "select username from listener where username =="+str(usrname)
	cursor.execute(query)
	addtolist2(cursor, a, 5)
	query = "select artisticname from artist where username =="+str(usrname)
	cursor.execute(query)

	query = "select title from playlist where username =="+str(usrname)
	cursor.execute(query)

	query = "select count(*) from song as a , playlist as t where t.username == a.artist and song.username =="+str(usrname)
	cursor.execute(query)


'''
def addtolist3(cur,a):
	for i in cur:
		mydict = {}
		mydict["username"] = i[0]
		a.append(mydict)

@app.route("/follower")
def follower():
	a=[]
	username = request.args.get("username")
	query = "select follower from follow where following ='"+str(username)+"';"
	cursor.execute(query)
	addtolist3(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

@app.route("/following")
def following():
	a=[]
	username = request.args.get("username")
	query = "select following from follow where follower ='"+str(username)+"';"
	cursor.execute(query)
	addtolist3(cursor, a)
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