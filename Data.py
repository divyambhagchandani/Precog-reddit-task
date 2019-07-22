import urllib3, json, praw
import pandas as pd
import datetime as dt
key="oHTDjY6PXRFS8Z1wBcDXELm5xy4" #(Secret)
user_key="OIO_pHHa-LQfHA"
username="divyamb29"
# password="supcha"
# app_name="precog"

# flairs=['Reddiquette', 'Politics', 'Science Technology', 'Dominant Policy', 'AskIndia', 'Food', 'Removed', 'Business/Finance', 'Business Finance Policy', 'Scheduled', 'Sports', 'Policy Economy', 'Non-Political', 'Photography','AMA']
flairs = ["AskIndia", "Non-Political", "[R]eddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]
reddit = praw.Reddit(client_id=user_key,
                     client_secret=key,
                     user_agent=username)
subreddit = reddit.subreddit('india')
x=[]
# flairs=[]
for flair in flairs:
	print(flair)
	a=[]
	for submission in subreddit.search(flair, limit=None):
		a.append(submission.title)
	x.append(a)
print(x)
for i in range(len(x)):
	print(flairs[i],len(x[i]))
# client = pymongo.MongoClient("mongodb+srv://admin:<divyam>@precog-z500c.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test
# url = "https://www.reddit.com/r/india/top.json"
# http = urllib3.PoolManager()
# response = http.request('GET', url)
# data = json.loads(response.data.decode('utf-8'))
# print (data)