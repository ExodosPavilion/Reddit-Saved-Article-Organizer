import json, io, praw

POST_GET_LIMIT = 5
#can be None

#https://github.com/bd-git/praw-get-saved-posts/blob/master/grabdata.py
#same thing i want to do but with databases mixed in

def loadData():
        with open("data.json", "r") as read_file:
            data = json.load(read_file)

        return data['CLIENT_ID'], data['SCRIPT_NAME'], data['CLIENT_SECRET'], data['CLIENT_USERNAME'], data['CLIENT_PASSWORD']


def getSaved(redditMain, username):
	#TODO: get all posts/comments that are saved
	savedPosts = redditMain.redditor(name=username).saved(limit=POST_GET_LIMIT)
	#savedPosts = redditMain.user.get_saved()
	#savedPosts = redditMain.user.get_saved(limit=None)
	
	return savedPosts
	
	
def prettyPrintPost():
	#TODO: Print out post details 
	
	return None
	
CLIENT_ID, SCRIPT_NAME, CLIENT_SECRET, CLIENT_USERNAME, CLIENT_PASSWORD = loadData()

reddit = praw.Reddit(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, username = CLIENT_USERNAME, password = CLIENT_PASSWORD, user_agent = 'anything')

print('Loading Data for ' + CLIENT_USERNAME)

rawData = getSaved(reddit, CLIENT_USERNAME)
posts = []

for i in rawData:
	posts.append(i)

print(posts)