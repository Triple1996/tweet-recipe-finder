from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import random
import sys
import flask
import os

# import API keys
consumer_key=os.environ['API_KEY']
consumer_secret=os.environ['API_SECRET_KEY']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

# establish auth token
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

# list of foods to choose from
foods = ['Roast Turkey', 'Stuffing', 'Pecan Pie', 'Sweet Potato Casserole', 'Mashed Potatoes', 'Turkey Gravy', 'Cheesecake']

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    
    # choose random food and query twitter
    randFood = random.choice(foods)
    result = auth_api.search(q=randFood, lang = "en", count=5)
    
    # if result is empty, pick a new food and query again
    while len(result) < 1:
        randFood = random.choice(foods)
        result = auth_api.search(q=randFood, lang = "en", count=5)
    
    # randomly select a tweet from list of results
    tweet = random.choice(result)
    
    # using tweet id, return "extended" text and print full_text
    status = auth_api.get_status(tweet.id, tweet_mode="extended")
    try:    
        tweetText = status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        tweetText = status.full_text
        
    # extract author and date/time published
    tweetAuthor = tweet.user.name
    tweetDate = tweet.created_at
    
    # pass parameters to flask to render webpage
    return flask.render_template(
        "index.html",
        tweet=tweetText,
        food=randFood,
        author=tweetAuthor,
        date=tweetDate
        )
    
app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
)
