#coding=utf-8
import re
import twitter
import tweepy
import time
from AuthConfig import *

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


user = "w0_3k"

if __name__=="__main__":
    auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
    auth.set_access_token(AccessToken, AccessTokenSecret)

    # api = tweepy.API(auth, proxy="127.0.0.1:1080")    # proxy
    api = tweepy.API(auth)
    # limit = api.rate_limit_status()['remaining_hits']
    # print 'you have', limit, 'API calls remaining until next hour'

    # for follower in tweepy.Cursor(api.followers).items():
    #     print follower.screen_name
    for friend in tweepy.Cursor(api.friends, id=user).items():
        print friend.screen_name,friend.id