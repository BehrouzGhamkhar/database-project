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


def addtolist4(cur,a):
	for i in cur:
		mydict = {}
		mydict["length"] = i[0]
		mydict["artist"] = i[1]
		mydict["title"] = i[2]
		a.append(mydict)


@app.route("/albumsongs")
def albumsongs():
	a=[]
	title = request.args.get("title")
	query = "select length,artist,title from song where albumtitle ='"+str(title)+"';"
	cursor.execute(query)
	addtolist4(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj


def addtolist5(cur,a):
	for i in cur:
		mydict = {}
		mydict["length"] = i[0]
		mydict["artist"] = i[1]
		mydict["title"] = i[2]
		mydict["date_added"] = str(i[3])
		mydict["album"] = i[4]
		a.append(mydict)

@app.route("/playlistsongs")
def playlistsongs():
	a=[]
	title = request.args.get("title")
	query = "select length,addsong.artist,songtitle,dateadded,addsong.albumtitle from addsong inner join song on addsong.songtitle = song.title where  playlisttitle ='"+str(title)+"';"
	cursor.execute(query)
	addtolist5(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist6(cur,a):
	for i in cur:
		mydict = {}
		mydict['title'] = i[0]
		mydict['artist'] = i[1]
		mydict['listener'] = i[2]
		a.append(mydict)

@app.route("/followingfeed")
def followingfeed():
	a=[]
	username = request.args.get("username")
	query = "select songtitle, artist, following from follow inner join play on follow.following = play.username where follow.follower = '" + str(username) + "' and play.dateplayed = (select max(dateplayed) from follow inner join play on follow.following = play.username where follow.follower = '" + str(username) + "');"
	cursor.execute(query)
	addtolist6(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist13(cur,a):
	for i in cur:
		mydict = {}
		mydict['artist'] = i[0]
		a.append(mydict)

@app.route("/suggestnational")
def suggestnational():
	a = []
	username = request.args.get("username")
	query = "select artist.username from artist inner join user on artist.username = user.username where nationality = (select nationality from user where username = '" + str(username) + "');"
	cursor.execute(query)
	addtolist13(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist14(cur,a):
	for i in cur:
		mydict = {}
		mydict['artist'] = i[0]
		mydict['number of songs'] = i[1]
		a.append(mydict)

@app.route("/artistbyactivity")
def artistbyactivity():
	a = []
	query = "select artist, count(title) from song group by artist order by count(title) desc;"
	cursor.execute(query)
	addtolist14(cursor,a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist15(cur,a):
	for i in cur:
		mydict = {}
		mydict['artist'] = i[0]
		mydict['songs per day'] = float(i[1])
		a.append(mydict)
#15
@app.route("/lazyartist")
def lazyartist():
	a = []
	query = "select username, count(song.title)/((2020-debutyear)*365) as result from artist inner join song on artist.username = song.artist  group by artist order by result asc;"
	cursor.execute(query)
	addtolist15(cursor,a)
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