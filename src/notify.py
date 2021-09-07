import tweepy
from config import get_twitter_creds

creds = get_twitter_creds()

def auth_api():
    auth = tweepy.OAuthHandler(
        consumer_key=creds.consumer_key,
        consumer_secret=creds.consumer_secret,
    )
    auth.set_access_token(creds.access_token_key, creds.access_token_secret)
    return tweepy.API(auth)

def create_tweet(tweet: str):
    api = auth_api()
    api.update_status(tweet)

def send_dm(msg: str, recipient_id: str):
    api = auth_api()
    api.send_direct_message(recipient_id=recipient_id, text=msg)
