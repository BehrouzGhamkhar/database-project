from flask import Flask ,redirect,url_for,render_template,request
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ghon",
        database = "database_project"
    )

cursor = db.cursor()

@app.route("/debug")
def debug():
	username = request.args.get("username")
	return getfivelatest(username)

def spec1(cur,a):
	for i in cur:
		return str(i[1])

def mainArtistGenre(username):
	a = []
	query = "select artist, genre, count(genre) from album where artist = '" + username + "' group by artist, genre order by count(genre) desc limit 1;"
	cursor.execute(query)
	return spec1(cursor,a)

def spec2(cur,a):
	for i in cur:
		return str(i[2])

def mainPlaylistGenre(playlist,owner):
	a = []
	query = "select playlisttitle, playlistowner, genre, count(genre) from addsong inner join album on addsong.albumtitle = album.title where playlisttitle = '" + playlist + "' and playlistowner = '" + owner + "' group by playlisttitle,playlistowner,genre order by count(genre) desc limit 1;"
	cursor.execute(query)
	return spec2(cursor, a)



def spec3(cur,a):
	for i in cur:
		return str(i[0])

def favartist(username):
	a=[]
	query ="select play.artist , count(songtitle) as cnt from play inner join song on play.songtitle = song.title where play.username ='"+username+"' group by play.artist order by cnt desc limit 1;"
	cursor.execute(query)
	return spec3(cursor,a)

def spec4(cur,a):
	for i in cur:
		return str(i[0])

def favoritelistenergenre(username):
	a = []
	query = "select genre, count(genre) from play inner join album on play.albumtitle = album.title where play.username = '" + username + "' group by genre order by count(genre) desc limit 1;"
	cursor.execute(query)
	return spec4(cursor, a)

def spec5(cur,a):
	for i in cur:
		mydict = {}
		mydict['title'] = i[0]
		mydict['artist'] = i[1]
		mydict['release date'] = str(i[2])
		a.append(mydict)
	return a

def getfivelatest(username):
	a = []
	query = "select song.title, song.artist, releasedate from song inner join album on song.albumtitle = album.title and song.artist = album.artist where song.artist = '" + username + "' order by releasedate desc limit 5;"
	cursor.execute(query)
	return spec5(cursor, a)


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
		mydict['date played'] = str(i[3])
		a.append(mydict)

@app.route("/followingfeed")
def followingfeed():
	a=[]
	username = request.args.get("username")
	query = "select songtitle, artist, temp.username, temp.mdate from play inner join(select username, max(dateplayed) as mdate from play where username in (select following from follow where follower = '" + str(username) + "') group by username order by max(dateplayed) desc) as temp on play.username = temp.username and play.dateplayed = temp.mdate;"
	cursor.execute(query)
	addtolist6(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist7(cur,a):
	templist = []
	for i in cur:
		templist.append(i[0])
	for i in templist:
		tempresult = getfivelatest(i)
		[a.append(j) for j in tempresult]
		

@app.route("/getlatestfollowingfivesongs")
def getlatestfollowingfivesongs():
	a = []
	username = request.args.get("username")
	query = "select username from artist inner join follow on username = following where follower = '" + username + "';"
	cursor.execute(query)
	addtolist7(cursor, a)
	return json.dumps(a)

def addtolist8(cur,a):
	for i in cur:
		a.append(i[0])
		
@app.route("/suggestartist")
def suggestartist():
	a = []
	username = request.args.get("username")
	favoriteArtist = favartist(username)
	maingenre = mainArtistGenre(favoriteArtist)
	query = "select username from artist where username not in (select following from follow where follower = '" + username + "') and username not in ('" + username + "');"
	cursor.execute(query)
	addtolist8(cursor, a)
	mydict = {}
	for i in a:
		if(mainArtistGenre(i) == maingenre):
			mydict['artist'] = i
			break
	jsonObj = json.dumps(mydict)
	return jsonObj

def addtolist9(cur,a):
	for i in cur:
		mydict = {}
		mydict['title'] = i[0]
		mydict['times played'] = i[1]
		a.append(mydict)

@app.route("/hitsongsoftheweek")
def hitsongsoftheweek():
	a = []
	query = "select songtitle, count(songtitle) from play where datediff(curdate(),dateplayed) <= 7 group by(songtitle) order by count(songtitle) desc limit 5;"
	cursor.execute(query)
	addtolist9(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist10(cur,a,querytype):
	for i in cur:
		mydict = {}
		if(querytype==1):
			mydict['title'] = i[0]
			mydict['release date'] = str(i[1])
		elif(querytype==2):
			mydict['title'] = i[0]
			mydict['times played'] = i[1]
		a.append(mydict)

@app.route("/suggestonfavorite")
def suggestonfavorite():
	a = []
	username = request.args.get("username")
	favoritegenre = favoritelistenergenre(username)
	query = "select song.title, releasedate from song inner join album on song.artist = album.artist and song.albumtitle = album.title where genre = '" + favoritegenre + "' order by releasedate desc limit 5;"
	cursor.execute(query)
	addtolist10(cursor, a,1)
	query = "select songtitle, count(songtitle) from play inner join album on play.albumtitle = album.title and play.artist = album.artist where genre = '" + favoritegenre + "' group by songtitle order by count(songtitle) desc limit 5;"
	cursor.execute(query)
	addtolist10(cursor, a,2)
	jsonObj = json.dumps(a)
	return jsonObj

def addtolist11(cur,a):
	for i in cur:
		mydict = {}
		mydict['title'] = i[0]
		mydict['artist'] = i[1]
		mydict['genre'] = i[2]
		a.append(mydict)

@app.route("/recommendbyplaylist")
def recommendbyplaylist():
	a = []
	name = request.args.get("name")
	owner = request.args.get("owner")
	maingenre = mainPlaylistGenre(name, owner)
	query = "select song.title, song.artist, genre from song inner join album on song.albumtitle = album.title where genre = '" + maingenre + "' and (song.title not in (select songtitle from addsong where playlisttitle = '" + str(name) + "' and playlistowner = '" + str(owner) + "') or song.artist not in (select artist from addsong where playlisttitle = '" + str(name) + "' and playlistowner = '" + str(owner) + "')) order by RAND() limit 2;"
	cursor.execute(query)
	addtolist11(cursor, a)
	jsonObj = json.dumps(a)
	return jsonObj



def addtolist12(cur,a):
	for i in cur:
		#mydict = {}
		a.append(i[0])

@app.route("/fans")
def fans():
	a=[]
	artist = request.args.get("username")
	artistgenra = mainArtistGenre(artist)
	query = "select play.username , count(songtitle) as cnt from play inner join song on play.songtitle = song.title where play.artist ='"+artist+"' group by play.username having cnt >= 10 order by cnt desc;"
	cursor.execute(query)
	addtolist12(cursor, a)
	b=[]
	for i in a:
		if(favoritelistenergenre(i) == artistgenra):
			mydict = {}
			mydict['listener'] = i
			b.append(mydict)

	jsonObj = json.dumps(b)
	return jsonObj





def addtolist13(cur,a):
	for i in cur:
		mydict = {}
		mydict['title'] = i[0]
		mydict['artist'] = i[1]
		a.append(mydict)

@app.route("/suggestnational")
def suggestnational():
	a = []
	username = request.args.get("username")
	query = "select title, artist from album inner join user on album.artist = user.username where nationality in (select nationality from user where username = '" + str(username) + "');"
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
		mydict['total songs'] = i[1]
		mydict['debut release date'] = str(i[2])
		mydict['activity'] = str(i[3])
		a.append(mydict)

@app.route("/lazyartists")
def lazyartist():
	a = []
	query = "select tempsong.artist, tempsong.titlecount, tempalbum.minreleasedate, tempsong.titlecount/datediff(curdate(),tempalbum.minreleasedate) as activity from (select artist, min(releasedate) as minreleasedate from album group by artist) as tempalbum inner join (select artist, count(title) as titlecount from song group by artist) as tempsong on tempsong.artist = tempalbum.artist where titlecount/datediff(curdate(),minreleasedate)<=0.03;"
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