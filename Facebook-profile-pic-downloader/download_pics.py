import facebook
import urllib
import os


graph= facebook.GraphAPI("<Access Token from Developers page>")
#get the likes data with field "link" from which we extract username
likes= graph.get_connections("<node id>", "likes?fields=link,name&limit=5000")


for i in range (0,len(likes["data"])):
    #GraphAPI returns a different id. So, we can't use this to call profile picture.
    nodeid= likes["data"][i]["id"]
    #returns name as it appreas on friends' timeline
    nodename= likes["data"][i]["name"]
    #returns friends' profilr page link. From which we extract username
    nodelink= likes["data"][i]["link"]
    #'https://www.facebook.com/suryateja.cheedella' It may return like this, for example
    #get username from link returned
    username= nodelink[25:]
    
    #because to user settings, it may not return username for some pics.
    #we check them and don't attempt to download them. (which we can't, actually)
    #'https://www.facebook.com/profile.php?id=100005090622885' It looks similar to this. Frrom which we can't extract username.
    check= (username[:7])
    if(check == "profile"):
        print("Can't fetch username due to their settings. :( ")
        continue
    
    #If you are planning to get likes from two or more nodes, You may have repeated likes. same friend liked both nodes.
    #so, we check and try not to re-download it. Which saves time.
    if (os.path.exists("fb/likers/"+nodename+".jpg")):
        print("Already downloaded "+nodename+"'s picture!")
        continue
    
    #print(username)
    #print(nodeid)
    print("Fetching "+nodename+"'s picture")
    #print(nodelink)
    
    #Use username to fetch picture with height 9000 pixels. Returns full size image
    pic= graph.get_connections(username, "picture?height=9000&redirect=false")
    #Takes two arguments, pic url and relative path to save the file
    urllib.request.urlretrieve(pic["data"]["url"], "fb/likers/"+nodename+".jpg")
    print("Downloaded the pic.")
