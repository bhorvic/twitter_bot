import tweepy

#This is basically a dead file from my first attempt at building a twitter bot
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

client = tweepy.client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)