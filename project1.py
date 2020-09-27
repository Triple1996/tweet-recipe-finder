from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
from os.path import join, dirname
from dotenv import load_dotenv
import random
import sys
import flask
import os
import requests

# grab .env variables without having to run "source project1.env"
dotenv_path = join(dirname(__file__), 'project1.env')
load_dotenv(dotenv_path)

# import API keys
consumer_key=os.environ['KEY']
consumer_secret=os.environ['KEY_SECRET']
access_token=os.environ['TOKEN']
access_token_secret=os.environ['TOKEN_SECRET']
api_key=os.environ['API_KEY']

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
    tweepyResult = auth_api.search(q=randFood, lang = "en", count=10)
    
    # if tweepyResult is empty, pick a new food and query again
    while len(tweepyResult) < 1:
        randFood = random.choice(foods)
        tweepyResult = auth_api.search(q=randFood, lang = "en", count=10)
    
    # randomly select a tweet from list of results
    tweet = random.choice(tweepyResult)
    
    # using tweet id, return "extended" text and print full_text
    status = auth_api.get_status(tweet.id, tweet_mode="extended")
    try:    
        tweetText = status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        tweetText = status.full_text
        
    # extract author and date/time published
    tweetAuthor = tweet.user.name
    tweetDate = tweet.created_at
 
    # query spoonacular recipes
    foodsList = requests.get('https://api.spoonacular.com/recipes/complexSearch?query='+randFood+'&apiKey='+api_key+'&number=3').json()
    food = random.choice(foodsList['results'])
    
    foodTitle = food['title']
    foodImg = food['image']
    foodId = food['id']
    
    # get recipe info using id
    recipe = requests.get('https://api.spoonacular.com/recipes/'+str(foodId)+'/information?apiKey='+api_key).json()
    
    recipeLink = recipe['spoonacularSourceUrl']
    
    # populate array of ingredients
    ingredients = []
    for ingredient in recipe['extendedIngredients']:
        ingredients.append(ingredient['originalString'])
    
    # params dict
    d = {
        'tweet':tweetText,
        'food':randFood,
        'author':tweetAuthor,
        'date':tweetDate,
        'foodTitle':foodTitle,
        'foodImg':foodImg,
        'len':len(ingredients),
        'ingredients':ingredients,
        'recipeLink':recipeLink
    }
        
    # pass parameters to flask to render webpage
    return flask.render_template(
        "index.html",
        **d
    )
    
app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
)
