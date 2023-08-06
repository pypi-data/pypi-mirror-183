import requests


# 4 main functions

def gimme(): # Basic gimme function to get a random meme
    response = requests.get("https://meme-api.com/gimme")
    json_data = (response.json())
    return json_data

def gimmenum(number:int)-> None:
    """Specify a number, to get said number of memes [max 50]""" # Takes a number, max is 50
    response = requests.get("https://meme-api.com/gimme/"+str(number))
    json_data = (response.json())
    return json_data

def specifysub(subreddit:str)->None:
    """Specify a subreddit to grab images from(do not use r/ simply the sub name) [single argument]""" #Takes a subreddit as an argument
    response = requests.get("https://meme-api.com/gimme/"+subreddit)
    json_data = (response.json())
    return json_data

def subnum(subreddit:str,number:int)->None:
    """Specify a subreddit and a custom number of memes to get from that sub [max sub:1, max num:50]""" # Takes a subreddit and a number as argument
    response = requests.get("https://meme-api.com/gimme/"+subreddit+"/"+str(number))
    json_data = (response.json())
    return json_data

#print(gimme())


#x = gimmenum(2)
#for i in x['memes']:
    #print(i['url'])

#print(specifysub('okbuddyretard'))

#x = subnum('okbuddyretard',3)
#for i in x['memes']
#   print(i['url'])