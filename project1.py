from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import flask
import os

consumer_key=os.environ['API_KEY']
consumer_secret=os.environ['API_SECRET_KEY']
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

foods = ['Lasagna', 'Gyro', 'Smoked Salmon', 'Taco', 'Burger', 'Quesadilla', 'Hot Dog']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

result = auth_api.search(q='Halo Infinite', count=1)
tweet = result[0].text


app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():

    return flask.render_template(
        "index.html",
        foods=foods,
        lenFoods=len(foods),
        tweet=tweet
        )
    
app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
)
