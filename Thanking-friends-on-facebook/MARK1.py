import facebook

graph = facebook.GraphAPI('Access token you got from facebook developers page')
feed = graph.get_connections("me", "feed?limit=200")
for a in range (0,200):
    post = feed["data"][a]
    fromDetails = (post["from"])
    fromName = fromDetails["name"]
    graph.put_like(post["id"])
    graph.put_object(post["id"], "comments", message="Thank you :d" + fromName)