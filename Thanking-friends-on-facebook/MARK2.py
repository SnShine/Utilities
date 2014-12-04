'''
	Author: Surya teja Cheedella
'''

import facebook

#get access token from facebook. It has a lifespan of around 1 hour
graph = facebook.GraphAPI('<Access Token>')
#fetching your timeline posts. limit upto 500 latest posts
feed = graph.get_connections("me", "feed?limit=500")

'''
    If you are facing any access token error while implementing, 
    try passing "feed" instead of "feed?limit=500"
'''

for a in range (0,500):
    post = feed["data"][a]
    time = post["created_time"]
    if time[0:10] == "2014-10-28":               #date of the post you wanted to comment on, 
	fromDetails = (post["from"])       	 #usually your birthday in this format yyyy-mm-dd
    	fromName = fromDetails["name"]           #name of friend who has posted
    	graph.put_like(post["id"])
    	print ("liked "+fromName+"'s post")		 #like that post
    	graph.put_object(post["id"], "comments", message="Thank you :D " + fromName)     #comment on that post
    	print ("commented on "+fromName+"'s post")
    else:
    	print("Sucessfully completed commenting on "+str(a)+" posts!")
    	break
    	
