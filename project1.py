from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import random
import sys
import flask
import os

consumer_key=os.environ['API_KEY']
consumer_secret=os.environ['API_SECRET_KEY']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

foods = ['Lasagna', 'Philly Cheese Steak', 'Smoked Salmon', 'Chicken Tikka Masalaa', 'Hamburger', 'Quesadilla', 'Filet Mignon']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    
    randFood = random.randint(0,6)
    result = auth_api.search(q=foods[randFood], lang = "en", count=10)
    randI = random.randint(0, 4)
    while len(result) < randI+1:
        result = auth_api.search(q=foods[randFood], lang = "en", count=10)
    randI = random.randint(0, 4)
    tweet = result[randI].text
    user = result[randI]


    return flask.render_template(
        "index.html",
        tweet=tweet,
        food=foods[randFood]
        )
    
app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
)
