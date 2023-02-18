import json
import requests
import pandas as pd
from datetime import datetime
import os
import snscrape.modules.twitter as sntwitter

def run_etl():
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Creating list to append tweet data 
    tweets_list = []

    # Tweet criteria
    handle = 'ZelenskyyUa'
    start_date = '2022-02-24'
    include = ["replies", "retweets"]

    # Format query
    query = "from:" + handle + " since:" + start_date
    for i in include:
        query += " include:" + i

    # Get tweets
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()): 
            
        #declare the attributes to be returned
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.lang, tweet.replyCount,tweet.retweetCount, tweet.likeCount, tweet.user.username])
        
    # Creating a dataframe from the tweets list above 
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Language', 'ReplyCount','RetweetCount','LikeCount', 'Username'])

    tweets_df.to_json(CUR_DIR + "/" + 'tweets-json.json')