#Importing tweepy, a python library for interacting with the twitter API
import tweepy

#Declare credentials as variables (actual keys and tokens not included in this file for security reasons)
#Keys and tokens are stored locally in a separate file
api_key = ""
api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

#Using tweepy to authenticate with twitter (basically stolen from the tutorial I was following to build this bot)
def api():
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	return tweepy.API(auth)
	
#This is the function that actually tweets
def tweet(api: tweepy.API, message: str, image_path=None):
	if image_path:
		api.update_status_with_media(message, image_path)
	else:
		api.update_status(message)
	#This is just the output from the tutorial I was following to build this bot	
	print('Tweeted successfully!')
	
	
#image.jpg is stored in a different directory because I kept getting errors while running this with the file in the same directory
if __name__ == '__main__':
	api = api()
	tweet(api, 'This was tweeted with python', 'image.jpg')

#All of the code here works, but I keep getting a 403 forbidden error when I try to run it because from what I can tell,
#I need elevated access to the API, which I am stuck on because I can't figure out how to apply or if I even am able to because Elon's a bitch