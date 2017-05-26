#coding=utf-8
import re
import twitter
import simplejson
import tweepy
import time
from AuthConfig import *

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
user = "w0_3k"
# api = tweepy.API(auth, proxy="127.0.0.1:1080")    # proxy
api = tweepy.API(auth)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print "RateLimitError! Sleep ..."
            # time.sleep(15 * 60)
            time.sleep(50)
            # api = tweepy.API(auth)
        except tweepy.TweepError:
            print tweepy.TweepError
            continue


if __name__=="__main__":

    # limit = api.rate_limit_status()['remaining_hits']
    # print 'you have', limit, 'API calls remaining until next hour'

    needCrawled = []
    crawled = []
    with open("./user/crawled") as f:
        for line in f:
            crawled.append(int(line.strip()))
    with open("./user/needCrawled") as f:
        for line in f:
            needCrawled.append((line.strip()))

    while needCrawled:
        f = open("./data/needCrawled",'w')
        for id in needCrawled:
            f.write(str(id))
            f.write("\n")
        f.close()

        for id in needCrawled:
            currentID = id
            needCrawled.remove(id)

            if id not in crawled:   # 未爬过
                print "craw:", id, "..."
                path = "./data/" + str(currentID)
                f = open(path, 'w')
                # follower
                for follower in limit_handled(tweepy.Cursor(api.followers,id=currentID).items(500)):
                    s = str(follower.id) + "\t" + str(currentID) + "\n"
                    needCrawled.append(follower.id)
                    f.write(s)

                # followee
                for friend in limit_handled(tweepy.Cursor(api.friends, id=currentID).items(500)):
                    s = str(currentID) + "\t" + str(friend.id) + "\n"
                    needCrawled.append(follower.id)
                    f.write(s)
                crawled.append(currentID)
                f.close()

        f = open("./data/crawled",'w')
        for id in crawled:
            f.write(str(id))
            f.write("\n")
        f.close()
