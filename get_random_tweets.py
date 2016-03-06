# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

import time
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'access-token'
ACCESS_SECRET = 'access-secret'
CONSUMER_KEY = 'cons-key'
CONSUMER_SECRET = 'cons-secret'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample(language='en')

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 

j = 10
num_tweets = 100000


for alpha in range(0, j):
    tweet_count = num_tweets
    moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
    file = "./raw_data/raw_" + moment + ".txt"
    f = open(file, 'w')

    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        f.write(json.dumps(tweet))
        f.write("\n")
        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break

    f.close()
