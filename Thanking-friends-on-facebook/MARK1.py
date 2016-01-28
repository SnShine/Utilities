'''
By Surya Teja Cheedella
BITS Pilani, Hyderabad Campus
'''


import facebook

#getting access token from facebook. It has a lifespan of 1 hour
graph = facebook.GraphAPI('Access token you got from facebook developers page')
#fetching your timeline posts. limit upto 200 latest posts
feed = graph.get_connections("me", "feed?limit=200")
#for every post on your timeline
for a in range (0,200):
    post = feed["data"][a]
    fromDetails = (post["from"])
    fromName = fromDetails["name"]           #name of friend who has posted
    graph.put_like(post["id"])				 #like that poist
    graph.put_object(post["id"], "comments", message="Thank you :d" + fromName)     #comment on that post
