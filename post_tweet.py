import tweepy
import os
from datetime import datetime, timezone
from collections import defaultdict

 
def spacesepstr2dateobjdefdict(sss):
    dsd = defaultdict(list)
    for line in sss.split('\n'):
        d_s, text = line.strip().split('    ')
        date_obj = datetime.strptime(d_s, "%Y%m%d").date()
        dsd[date_obj].append(text)

    return dsd


def spacesepstr2todaystext_l(sss):
    date_obj = datetime.now(timezone.utc).date()
    dsd = spacesepstr2dateobjdefdict(sss)
    return dsd[date_obj]


def make_tweepy_client():
    ckey = os.environ.get('CONSUMER_KEY')
    csec = os.environ.get('CONSUMER_SECRET')
    akey = os.environ.get('ACCESS_KEY')
    asec = os.environ.get('ACCESS_SECRET')
    client = tweepy.Client(consumer_key=ckey, consumer_secret=csec, 
                           access_token=akey, access_token_secret=asec)

    return client


def main(event, context):
    """event, context are automatically passed from the pub/sub trigger.
    TODO: move tweet to the publish of the pub/sub chron??"""
  
    sss = """20220128    TEST
20220129    TEST2
20220130    TEST3"""

    todays_tweets = spacesepstr2todaystext_l(sss)
    client = make_tweepy_client()
    post_info = []
    for tweet in todays_tweets:
        resp = client.create_tweet(text=tweet)
        post_info.append([resp, tweet])
    return post_info



if __name__ == '__main__':
    print(main())

