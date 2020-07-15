from flask import Flask ,request
import mysql.connector
import json
import hashlib
import random
import string

app = Flask(__name__)

db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ghon",
        database = "database_project"
    )

cursor = db.cursor()

def spec1(cur,a):
	for i in cur:
		return str(i[1])

def generatesalt():
	alphabet = string.ascii_letters + string.digits + string.punctuation
	result = "".join([random.choice(alphabet) for i in range(5)])
	return result

def generatepassword(inputpassword,salt):
	result = inputpassword + salt
	return hashlib.md5(result.encode()).hexdigest()

def checkpassword(inputpassword,salt,targetpassword):
	result = generatepassword(inputpassword, salt)
	return result==targetpassword

def playlistexists(title,username): #Check if the playlsit exists
	query = "select title from playlist where title = '" + title + "' and username = '" + username + "';" #Check if the playlist exists
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return False
	return True

def checkdate(inputdate):
	query = "select datediff('" + str(inputdate) + "',curdate());"
	cursor.execute(query)
	for i in cursor:
		if(i[0]<0): return False
		else: return True

def insertcreditcard(username, number, exp):
	query = "insert into creditcard values(" + str(number) + ",'" + exp + "','" + username + "');"
	cursor.execute(query)
	db.commit()

def deletecreditcard(username):
	query = "delete from creditcard where username = '" + username + "';"
	cursor.execute(query)
	db.commit()

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

def getfollowercnt(username):
	a=[]
	query = "select count(follower) from follow where following = '"+username+"';"
	cursor.execute(query)
	for i in cursor:
		return i[0]

def getfollowingcnt(username):
	a=[]
	query = "select count(following) from follow where follower = '"+username+"';"
	cursor.execute(query)
	for i in cursor:
		return i[0]


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

def viewqueryspec1(cur,a):
	for i in cur:
		mydict = {}
		mydict["username"] = i[0]
		mydict["first name"] = i[1]
		mydict["last name"] = i[2]
		a.append(mydict)

def viewqueryspec2(cur,a):
	for i in cur:
		mydict = {}
		mydict["username"] = i[0]
		mydict["artistic name"] = i[1]
		a.append(mydict)

def viewqueryspec3(cur,a):
	for i in cur:
		mydict = {}
		mydict["album title"] = i[0]
		mydict["release date"] = str(i[1])
		a.append(mydict)

def viewqueryspec4(cur,a):
	for i in cur:
		mydict = {}
		mydict["song title"] = i[0]
		mydict["song artist"] = i[1]
		a.append(mydict)

def viewqueryspec5(cur,a):
	for i in cur:
		mydict = {}
		mydict["playlist title"] = i[0]
		mydict["count songs"] = i[1]
		mydict["last update"] = str(i[2])
		a.append(mydict)

def viewqueryspec6(cur,a):
	for i in cur:
		mydict = {}
		mydict["followers"] = i[0]
		mydict["followings"] = i[1]
		a.append(mydict)


@app.route("/view")
def view():
	a=[]
	usrname = request.args.get("usrname")
	query = "select username , firstname, lastname from listener where username ='" + str(usrname) + "';"
	cursor.execute(query)
	viewqueryspec1(cursor, a)
	if(not a):
		query = "select username , artisticname from artist where username ='" +str(usrname)+ "';"
		cursor.execute(query)
		viewqueryspec2(cursor, a)
		a.append({"main genre" : mainArtistGenre(usrname)})
		albumquery = "select title , releasedate from album where artist ='" + str(usrname) +"' order by(releasedate) desc;"
		cursor.execute(albumquery)
		viewqueryspec3(cursor, a)
		
		popularSongsQuery= "select play.songtitle , play.artist , count(likesong.songtitle), count(play.songtitle) from play inner join likesong on play.artist = likesong.artist and play.songtitle = likesong.songtitle and play.username = likesong.username where play.artist = '"+usrname+"' group by likesong.songtitle order by count(likesong.songtitle) desc , count(play.songtitle) asc limit 3 ;" 
		cursor.execute(popularSongsQuery)
		viewqueryspec4(cursor, a)

	query = "select playlisttitle , count(songtitle) , max(dateadded) from addsong where playlistowner ='"+str(usrname)+"' group by playlisttitle;"
	cursor.execute(query)
	viewqueryspec5(cursor, a)

	followerquery = getfollowercnt(usrname)
	followingquery = getfollowingcnt(usrname)
	a.append({"followers" : followerquery})
	a.append({"followings" : followingquery})
	return json.dumps(a)

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

def addtolist16(cur,a):
	for i in cur:
		mydict = {}
		mydict['username'] = i[0]
		mydict['total length'] = int(i[1])/3600
		mydict['sign-up date'] = str(i[2])
		a.append(mydict)
	return(a)

@app.route("/sususer")
def sususer():
	a = []
	query = "select user.username, sum(length), signupdate from user inner join play inner join song on play.artist = song.artist and play.songtitle = song.title and user.username = play.username where user.username not in (select username from premium) group by(username) having (sum(length)/datediff(curdate(),signupdate))/3600>=17 and (select count(follower) from follow where following = user.username)/(select count(following) from follow where follower = user.username)>5;"
	cursor.execute(query)
	addtolist16(cursor, a)
	return json.dumps(a)

def addtolist17(cur,a):
	for i in cur:
		mydict = {}
		mydict['username'] = i[0]
		a.append(mydict)


@app.route("/consistentuser")
def consistentuser():
	a=[]
	query = ''' select distinct follower from follow inner join 
	(select temp.username as usrname, temp.cnt , temp.signupdate from (select user.username , count(songtitle) as cnt , user.signupdate from user inner join play on user.username = play.username group by user.username) as temp where temp.cnt/datediff(curdate(),temp.signupdate) >= 1) as temp2
		on following = temp2.usrname;
	 '''
	cursor.execute(query)
	addtolist17(cursor,a)
	jsonObj = json.dumps(a)
	return jsonObj

#User Specs

@app.route("/releasealbum",methods=["POST"])
def releasealbum():
	title = request.args.get("title")
	artist = request.args.get("artist")
	genre = request.args.get("genre")

	query = "select isapproved from artist where username = '" + artist + "';"
	cursor.execute(query)
	for i in cursor:
		if(i[0]==0):
			return "You are not an approved artist yet.", 406
		break
		

	query = "select title from album where title = '" + title + "' and artist = '" + artist + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(a):
		return "This album already exists", 406
	
	query = "insert into album values('" + title + "','" + artist + "','" + genre + "', curdate());"
	cursor.execute(query)
	db.commit()
	return "Album added successfully", 201

@app.route("/deletealbum",methods=["POST"])
def deletealbum():
	title = request.args.get("title")
	artist = request.args.get("artist")

	query = "select title from album where title = '" + title + "' and artist = '" + artist + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "Album not found", 404

	query = "delete from album where title = '" + title + "' and artist = '" + artist + "';"
	cursor.execute(query)
	db.commit()
	return "Album deleted successfully" , 200

@app.route("/addsongtoalbum",methods=["POST"])
def addsongtoalbum():
	title = request.args.get("title")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	length = request.args.get("length")
	
	query = "select title,artist from song where title ='"+ title +"' and artist = '"+ artist +"';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(a):
		return "Duplicate song title." , 406


	query = "select title,artist from album where title ='"+ albumtitle +"' and artist = '"+ artist +"';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		genre = request.args.get("genre")
		if(genre is None):
			return " Please enter the genre of the song" , 406
		query = "insert into album values('"+ title +"','"+ artist +"','"+ genre +"', curdate());"
		cursor.execute(query)
		db.commit()
		query = "insert into song values('"+ title +"','"+ title +"','"+ artist +"','"+ length +"');"
		cursor.execute(query)
		db.commit()
		return "Song added to album successfully" ,201

	query = "insert into song values('"+ title +"','"+ albumtitle +"','"+ artist +"','"+ length +"');"
	cursor.execute(query)
	db.commit()
	return "Song added to album successfully" ,201



@app.route("/deletesongfromalbum",methods=["POST"])
def deletesongfromalbum():
	title = request.args.get("title")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	length = request.args.get("length")
	
	query = "select title,artist from album where title ='"+ albumtitle +"' and artist = '"+ artist +"';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "Album not found", 404

	query = "delete from song where title = '"+ title +"' and albumtitle = '"+ albumtitle +"' and artist = '"+ artist +"' and length = '"+ length +"';"
	cursor.execute(query)
	db.commit()
	return "Song deleted from album successfully" ,200



@app.route("/follow",methods=["POST"])
def follow():
	username = request.args.get("username")
	target = request.args.get("target")
	query = "insert into follow values('"+username+"','"+target+"');"
	cursor.execute(query)
	db.commit()
	return "followed successfully", 201

@app.route("/unfollow",methods=["POST"])
def unfollow():
	username = request.args.get("username")
	target = request.args.get("target")
	query = "delete from follow where follower ='"+username+"' and following ='"+target+"';"
	cursor.execute(query)
	db.commit()
	return "unfollowed successfully", 200

@app.route("/likesong",methods=["POST"])
def likesong():
	username = request.args.get("username")
	songtitle = request.args.get("songtitle")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	query = "insert into likesong values ('"+username+"','"+songtitle+"','"+albumtitle+"','"+artist+"') ;"
	cursor.execute(query)
	db.commit()
	return "song liked successfully", 201

@app.route("/unlikesong",methods=["POST"])
def unlikesong():
	username = request.args.get("username")
	songtitle = request.args.get("songtitle")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	query = "delete from likesong where username = '" + username + "' and songtitle = '" + songtitle + "' and albumtitle = '" + albumtitle + "' and artist = '" + artist + "';"
	cursor.execute(query)
	db.commit()
	return "song unliked successfully", 201

@app.route("/reportsong",methods=["POST"])
def reportsong():
	try:
		songtitle = request.args.get("songtitle")
		albumtitle = request.args.get("albumtitle")
		artist = request.args.get("artist")
		username = request.args.get("username")
		query = "insert into report values('" + songtitle + "','" + albumtitle + "','" + artist + "','" + username + "');"
		cursor.execute(query)
		db.commit()
		return "Song reported successfully", 201
	except:
		return "This song is already deleted"

@app.route("/playsong",methods=["POST"])
def playsong():
	username = request.args.get("username")
	songtitle = request.args.get("songtitle")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	query = "select username from premium where username = '"+ username +"';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i[0])
	if(not a):	
		query = "select count(songtitle) from play where username ='"+ username +"' and date(dateplayed) = curdate() ;"
		cursor.execute(query)
		for i in cursor:
			if int(i[0]) >=5:
				return "You can't play any more songs since you're not a premium user or your premium account has been expired.",406


	query = "insert into play values ('"+username+"',current_timestamp,'"+songtitle+"','"+albumtitle+"','"+artist+"') ;"
	cursor.execute(query)
	db.commit()
	return "song played successfully", 201

def checkplaylistaccess(title,owner,user):
	hasaccess = False
	query = "(select title from playlist where username = '" + user + "') union (select playlisttitle from adduser where username = '" + user + "' and playlistowner = '" + owner + "');"
	cursor.execute(query)
	a = []
	for i in cursor:
		if(str(i[0])==title):
			hasaccess = True
			break
	return hasaccess

@app.route("/addsongtoplaylist",methods=["POST"])
def addsongtoplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	songtitle = request.args.get("songtitle")
	albumtitle = request.args.get("albumtitle")
	artist = request.args.get("artist")
	adder = request.args.get("adder")

	if(playlistexists(playlisttitle,playlistowner)==False):
		return "Playlist not found", 404

	access = checkplaylistaccess(playlisttitle, playlistowner, adder) # Check if the adder has access to the playlist
	if(access==False):
		return "You don't have access to this playlist", 406
	
	query = "select songtitle from addsong where songtitle = '" + songtitle + "' and artist = '" + artist + "' and playlisttitle = '" + playlisttitle + "' and playlistowner = '" + playlistowner + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(a):
		return "This song already exists in this playlist!", 406

	query = "insert into addsong values(curdate(),'" + playlisttitle + "','" + playlistowner + "','" + songtitle + "','" + albumtitle + "','" + artist + "','" + adder + "');"
	cursor.execute(query)
	db.commit()
	return "Song added successfully", 201

@app.route("/removesongfromplaylist",methods=["POST"])
def removesongfromplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	songtitle = request.args.get("songtitle")
	artist = request.args.get("artist")
	user = request.args.get("username")

	if(playlistexists(playlisttitle,playlistowner)==False):
		return "Playlist not found", 404

	access = checkplaylistaccess(playlisttitle, playlistowner, user) # Check if the user has access to the playlist
	if(access==False):
		return "You don't have access to this playlist", 406

	query = "delete from addsong where playlisttitle = '" + playlisttitle + "' and playlistowner = '" + playlistowner + "' and songtitle = '" + songtitle + "' and artist = '" + artist + "';"
	cursor.execute(query)
	db.commit()
	return "Song removed successfully", 200

@app.route("/addusertoplaylist",methods=["POST"])
def addusertoplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	adder = request.args.get("adder")
	user = request.args.get("username")

	if(playlistexists(playlisttitle,playlistowner)==False):
		return "Playlist not found", 404

	query = "select username from user where username = '" + user + "';" #Check if the user exists
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "User not found",404

	if(adder!=playlistowner):
		return "You can't add users to this playlist, since you're not its owner", 406

	query = "select username from adduser where username = '" + user + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(a or user == playlistowner):
		return "The user you're trying to add is already in the playlist", 406

	query = "insert into adduser values('" + user + "','" + playlisttitle + "','" + playlistowner + "');"
	cursor.execute(query)
	db.commit()
	return "User was added successfully to the playlist", 201

@app.route("/removeuserfromplaylist",methods=["POST"])
def removeuserfromplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	remover = request.args.get("remover")
	user = request.args.get("username")

	if(playlistexists(playlisttitle,playlistowner)==False):
		return "Playlist not found", 404

	query = "select username from user where username = '" + user + "';" #Check if the user exists
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "User not found",404

	if(remover!=playlistowner):
		return "You can't remove users from this playlist, since you're not its owner",406

	if(user==playlistowner):
		return "You can't delete the playlist owner, try deleting the whole playlist", 406

	query = "select username from adduser where username = '" + user + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "The user you're trying to delete is already not in the playlist", 406

	query = "delete from adduser where username = '" + user + "' and playlisttitle = '" + playlisttitle + "' and playlistowner = '" + playlistowner + "';"
	cursor.execute(query)
	db.commit()
	return "User remvoed successfully", 200

@app.route("/likeplaylist",methods=["POST"])
def likeplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	user = request.args.get("username")

	try:
		query = "insert into likeplaylist values('" + user + "','" + playlisttitle + "','" + playlistowner + "');"
		cursor.execute(query)
		db.commit()
		return "Playlist liked successfully", 201
	except:
		return "Invalid parameters", 406

@app.route("/unlikeplaylist",methods=["POST"])
def unlikeplaylist():
	playlisttitle = request.args.get("playlist")
	playlistowner = request.args.get("owner")
	user = request.args.get("username")

	query = "delete from likeplaylist where username = '" + user + "' and playlisttitle = '" + playlisttitle + "' and playlistowner = '" + playlistowner + "';"
	cursor.execute(query)
	db.commit()
	return "Playlist unliked successfully", 200

@app.route("/buypremium",methods=["POST"])
def buypremium():
	try:
		username = request.args.get("username")
		duration = request.args.get("duration")
		cardnumber = request.args.get("cardnumber")
		cardexpdate = request.args.get("cardexpdate")

		query = "select number, expdate from creditcard where username = '" + username + "';" #Check if the user had previously bought a premium account
		cursor.execute(query)
		a = []
		for i in cursor:
			a.append((int(i[0]),i[1]))
		if(not a): #No credit card found, check the credit card user has entered
			if(checkdate(cardexpdate)==False):
				return "The credit card you've entered has an invalid expiration date", 406
			#if not, then it means that the user has entered a valid expiration date for the credit card
			insertcreditcard(username, cardnumber, cardexpdate)

		else: #The user had previously bought a premium account
			if(a[0][0]==int(cardnumber)):
				if(checkdate(a[0][1])==False):
					deletecreditcard(username)
					return "Your credit card has expired and was deleted from the system", 406
			else:
				return "Invalid credit card number", 406

		#if everything's fine, proceed to buy the premium account

		query = "select duration from premium where username = '" + username + "' ;" #Check if user's premium account still has some remaining duration
		cursor.execute(query)
		a = []
		response =""
		for i in cursor:
			a.append(i[0])
		if(a): #Increase the remaining time
			duration = int(a[0]) + int(duration)
			query = "update premium set duration = " + str(duration) + " where username = '" + username + "';"
			cursor.execute(query)
			db.commit()
			return response + "Premium account has been bought successfully", 201

		query = "insert into premium values ("+ str(duration) +",'"+ username +"',curdate()) ;"
		cursor.execute(query)
		db.commit()
		return response + "Premium account has been bought successfully", 201

	except :
		return "You don't have permission to buy premium account."
	
@app.route("/signup",methods=["POST"])
def signup():
	username = request.args.get("username")
	email = request.args.get("email")
	nationality = request.args.get("nationality")
	password = request.args.get("password")
	personalquestion = request.args.get("personalquestion")
	personalanswer = request.args.get("personalanswer")

	query = "select username from user where username = '" + username + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i[0])
	if(a):
		return "This username already exists.", 406

	query = "select email from user where email = '" + email + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i[0])
	if(a):
		return "This email already exists.", 406

	salt = generatesalt()
	password = generatepassword(password, salt)

	query = "insert into user values('" + username + "','" + email + "','" + nationality + "','" + password + "','" + personalquestion + "','" + personalanswer + "',curdate(),'" + salt + "');"
	cursor.execute(query)
	db.commit()
	return "Profile created successfully.", 201

@app.route("/aslistener",methods=["POST"])
def aslistener():
	username = request.args.get("username")
	firstname = request.args.get("firstname")
	lastname = request.args.get("lastname")
	yearofbirth = request.args.get("yearofbirth")
	
	try:
		query = "insert into listener values('" + username + "','" + firstname + "','" + lastname + "'," + yearofbirth + ");"
		cursor.execute(query)
		db.commit()
		return "Your listener account was created successfully", 201
	except:
		query = "select * from user where username = '" + username + "';"
		cursor.execute(query)
		a = []
		for i in cursor:
			a.append(i)
		if(not a):
			return "No corresponding user exists for this listener account.", 406

		query = "select * from listener where username = '" + username + "';"
		cursor.execute(query)
		a = []
		for i in cursor:
			a.append(i)
		if(a):
			return "A listener account corresponding to this username already exists.", 406

@app.route("/asartist",methods=["POST"])
def asartist():
	username = request.args.get("username")
	artisticname = request.args.get("artisticname")
	debutyear = request.args.get("debutyear")

	try:
		query = "insert into artist values('" + username + "','" + artisticname + "'," + debutyear + ",0);"
		cursor.execute(query)
		db.commit()
		return "Your artist account was created successfully", 201
	except:
		query = "select * from user where username = '" + username + "';"
		cursor.execute(query)
		a = []
		for i in cursor:
			a.append(i)
		if(not a):
			return "No corresponding user exists for this artist account.", 406

		query = "select * from artist where username = '" + username + "';"
		cursor.execute(query)
		a = []
		for i in cursor:
			a.append(i)
		if(a):
			return "An artist account corresponding to this username already exists.", 406
		

@app.route("/deleteprofile",methods=["POST"])
def deleteprofile():
	username = request.args.get("username")
	password = request.args.get("password")
	query = "select password, salt from user where username = '" + username + "';"

	'''
	cursor.execute(query)
	a = []
	for i in cursor:
		if password != i[0]:
			return "Wrong password!", 406
	'''
	query = "delete from user where username = '" + username + "' and password = '" + password + "';"
	cursor.execute(query)
	db.commit()
	return "Profile deleted successfully.", 200

@app.route("/login",methods=["POST"])
def login():
	username = request.args.get("username")
	password = request.args.get("password")

	query = "select username, password from user where username = '" + username + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append((i[0],i[1]))
	if(not a):
		return "Invalid username!", 406

	if(a[0][1]==password):
		if(a[0][0]=="admin"):
			return "Logged in successfully as admin", 200
		else:
			query = "select username from listener where username = '" + a[0][0] + "';"
			cursor.execute(query)
			temp = []
			for i in cursor:
				temp.append(i)
			if(temp):
				return "Logged in successfully as a listener", 200

			query = "select username from artist where username = '" + a[0][0] + "';"
			cursor.execute(query)
			for i in cursor:
				temp.append(i)
			if(temp):
				return "Logged in successfully as an artist", 200

			return "You should create a listener account or an artist account", 406

	else: #if password is wrong
		return "Wrong password!", 406

def checkplaylistcreation(title,username): #Checks if the user can create another playlist
	query = "select username from premium where username = '" + username + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)

	if(not a):
		query = "select count(title) from playlist where username = '" + username + "';"
		cursor.execute(query)
		for i in cursor:
			if(int(i[0])>=5):
				return False
	return True

@app.route("/createplaylist",methods=["POST"])
def createplaylist():
	title = request.args.get("title")
	username = request.args.get("username")
	
	access = checkplaylistcreation(title, username)
	if(access==False):
		return "You can't make another playlist, since you're not a premium user or your premium account has been expired.",406

	query = "select title from playlist where title = '" + title + "' and username = '" + username + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(a):
		return "A playlist with this name already exists.", 406

	query = "insert into playlist values('" + title + "','" + username + "');"
	cursor.execute(query)
	db.commit()
	return "Playlist created successfully", 201

@app.route("/deleteplaylist",methods=["POST"])
def deleteplaylist():
	title = request.args.get("title")
	username = request.args.get("username")
	query = "select title, username from playlist where title = '" + title + "' and username = '" + username + "';"
	cursor.execute(query)
	a = []
	for i in cursor:
		a.append(i)
	if(not a):
		return "No such playlist exists", 406
	query = "delete from playlist where title = '" + title + "' and username = '" + username + "';"	
	cursor.execute(query)
	db.commit()
	return "Playlist deleted successfully", 200

@app.route("/unapprovedartists",methods=["POST"])
def unapprovedartists():
	a=[]
	query= "select username , artisticname , debutyear  from artist where isapproved = 0 ; "
	cursor.execute(query)
	for i in cursor:
		myDict = {}
		myDict['username'] = i[0]
		myDict['artisticname'] = i[1]
		myDict['debutyear'] = i[2]
		a.append(myDict)

	return json.dumps(a)

@app.route("/approveartist",methods=["POST"])
def approveartist():
	username = request.args.get("username")
	query = "update artist set isapproved = 1 where username = '"+ username +"';"
	cursor.execute(query)
	db.commit()
	return "Artist approved successfully" , 201

@app.route("/unapproveartist",methods=["POST"])
def unapproveartist():
	username = request.args.get("username")
	query = "delete from user where username = '"+ username +"';"
	cursor.execute(query)
	db.commit()
	return "Unapproved artist account deleted by admin successfully" , 200

@app.route("/deleteaccbyadmin",methods=["POST"])
def deleteaccbyadmin():
	username = request.args.get("username")
	query = "delete from user where username = '"+ username +"';"
	cursor.execute(query)
	db.commit()
	return "Account deleted by admin successfully" , 200

@app.route("/deleteplaylistbyadmin",methods=["POST"])
def deleteplaylistbyadmin():
	username = request.args.get("username")
	title = request.args.get("title")
	query = "delete from playlist where username = '"+ username +"' and title = '"+ title +"';"
	cursor.execute(query)
	db.commit()
	return "Playlist deleted by admin successfully" , 200

@app.route("/deletealbumbyadmin",methods=["POST"])
def deletealbumbyadmin():
	artist = request.args.get("artist")
	title = request.args.get("title")
	query = "delete from album where title = '"+ title +"' and artist = '"+ artist +"' ;"
	cursor.execute(query)
	db.commit()
	return "Album deleted by admin successfully" , 200

@app.route("/getreportlist",methods=["POST"])
def getreportlist():
	query = "select songtitle , artist , count(songtitle) from report group by songtitle order by count(songtitle) ;"
	cursor.execute(query)
	a=[]
	for i in cursor:
		myDict={}
		myDict["songtitle"] = i[0]
		myDict["artist"] = i[1]
		myDict["count"] = i[2]
		a.append(myDict)

	return json.dumps(a)


@app.route("/ignorereportedsong",methods=["POST"])
def ignorereportedsong():
	artist = request.args.get("artist")
	songtitle = request.args.get("songtitle")

	query = "delete from report where artist ='" + artist + "' and songtitle ='" + songtitle + "';"
	cursor.execute(query)
	db.commit()

	return "Song ignored from report list by admin successfully", 200

@app.route("/deletereportedsong",methods=["POST"])
def deletereportedsong():
	artist = request.args.get("artist")
	title = request.args.get("title")

	query = "delete from song where artist ='" + artist + "' and title ='" + title + "';"
	cursor.execute(query)
	db.commit()

	return "Song deleted by admin successfully", 200


@app.route("/debug")
def debug():
	salt = generatesalt()
	return(generatepassword("abcdefghijklmnopqrstuvwxyz",salt))

if __name__ == "__main__":
	app.run(host ="localhost" , port =5000,debug=True)