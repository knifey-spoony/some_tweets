import tweepy
import os

def make_tweepy_client():
    ckey = os.environ.get('CONSUMER_KEY')
    csec = os.environ.get('CONSUMER_SECRET')
    akey = os.environ.get('ACCESS_KEY')
    asec = os.environ.get('ACCESS_SECRET')
    client = tweepy.Client(consumer_key=ckey, consumer_secret=csec, 
                           access_token=akey, access_token_secret=asec)

    return client


if __name__ == '__main__':
    client = make_tweepy_client()
    resp = client.create_tweet(text="TEST tweepy")
    print(resp.data)
