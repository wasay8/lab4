import praw
import pandas as pd
import argparse
import time
import random
def pulling_posts(num,subreddit):
	
	

	posts_dict = {"Title": [], "Post Text": [],
				"ID": [], "Score": [],
				"Total Comments": [], "Post URL": []
				}
	count = 0
	querys=["information","war","spy","states","India","machine","russia","?","lose","win",
	"university","education","top","money","business","AI","train","speed",
	"high","US","China","company","phone","update","language","apple","sun","hi","month","year","*"]
	random.shuffle(querys)
	methods = ["relevance"] # methods: hot top new
	for query in querys:
		for method in methods:
			posts = subreddit.search(query=query,sort=method,time_filter="all",limit=None)
			for post in posts:
				count +=1
				# Title of each post
				posts_dict["Title"].append(post.title)
				
				# Text inside a post
				posts_dict["Post Text"].append(post.selftext)
				
				# Unique ID of each post
				posts_dict["ID"].append(post.id)
				
				# The score of a post
				posts_dict["Score"].append(post.score)
				
				# Total number of comments inside the post
				posts_dict["Total Comments"].append(post.num_comments)
				
				# URL of each post
				posts_dict["Post URL"].append(post.url)
				if count>=num:
					top_posts = pd.DataFrame(posts_dict)
					print(f"{count} of {num} has been stored")
					return top_posts
			print(f"{count} of {num} has been stored")
	top_posts = pd.DataFrame(posts_dict)
	return top_posts
	# Saving the data in a pandas dataframe
	
	
def fetching(num):
		start_time = time.time()
		reddit_read_only = praw.Reddit(client_id="OZo48CIThXTgCEIegqPBWQ",		 # your client id
				client_secret="O6mXNbGUl-a2z-lj_Ywkp6APdrOEPw",	 # your client secret
				user_agent="dsci-560", # your user agent
				username="Hot-Bowler-6583",
				password="dsci-560ATM")	 

		
		subreddit = reddit_read_only.subreddit("tech")
		num_of_posts = num 
		
		posts_csv = pulling_posts(num_of_posts,subreddit)
		end_time = time.time()
		print("Data fetching Spend time:",end_time-start_time)
		return posts_csv
if __name__ == "__main__":
	fetching(num)
		
	
