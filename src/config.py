from dataclasses import dataclass
import os

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

@dataclass
class Credentials:
    consumer_key: str
    consumer_secret: str
    access_token_key: str
    access_token_secret: str

def get_twitter_creds():
    if not CONSUMER_KEY:
        raise ValueError("Twitter consumer key missing")
    if not CONSUMER_SECRET:
        raise ValueError("Twitter consumer secret missing")
    if not ACCESS_TOKEN:
        raise ValueError("Twitter access token missing")
    if not ACCESS_TOKEN_SECRET:
        raise ValueError("Twitter access token secret missing")
    return Credentials(
        consumer_key=CONSUMER_KEY, 
        consumer_secret=CONSUMER_SECRET, 
        access_token_key=ACCESS_TOKEN, 
        access_token_secret=ACCESS_TOKEN_SECRET,
    )
