import tweepy 
from key import *


auth=tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)

api=tweepy.API(auth)

api.update_with_media('in.pinterest.com.jpeg','Tweeting Lord Shiv with python ')
