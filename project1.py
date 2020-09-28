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
foods = ['Roast Turkey', 'Stuffing', 'Pecan Pie', 'Sweet Potato Casserole', 'Mashed Potatoes', 'Gravy', 'Cheesecake']

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
    try:
        code = foodsList['code']
    except KeyError:
        code = 200
        
    if (code == 402): # daily limit reached
        foodTitle = "We're sorry, Spoonacular's api limit has been reached. Try again tomorrow."
        foodImg = "http://i.stack.imgur.com/nLBGZ.png"
        recipeLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        cookTime = 0
        servingSize = 0
        ingredients = ["Even", "refreshing", "the", "page", "won't", "save", "you", "now"]
    else: # pull a recipe from results
        try:
            food = random.choice(foodsList['results'])
            foodTitle = food['title']
            foodImg = food['image']
            foodId = food['id']
            
            # get recipe info using id
            recipe = requests.get('https://api.spoonacular.com/recipes/'+str(foodId)+'/information?apiKey='+api_key).json()
            recipeLink = recipe['sourceUrl']
            cookTime = recipe['readyInMinutes']
            servingSize=recipe['servings']
            
            # populate array of ingredients
            ingredients = []
            for ingredient in recipe['extendedIngredients']:
                ingredients.append(ingredient['originalString'])
            
        except KeyError:
            foodTitle = "Oops! A recipe could not be found. Please try again."
            foodImg = "https://ih0.redbubble.net/image.363362205.4456/flat,550x550,075,f.u4.jpg"
            recipeLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            cookTime = 0
            servingSize = 0
            ingredients = ["Try", "refreshing", "the", "page", "to", "search", "again"]
        except IndexError: 
            foodTitle = "Oops! A recipe could not be found. Please try again."
            foodImg = "https://ih0.redbubble.net/image.363362205.4456/flat,550x550,075,f.u4.jpg"
            recipeLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            cookTime = 0
            servingSize = 0
            ingredients = ["Try", "refreshing", "the", "page", "to", "search", "again"]
        
    
    #foodTitle = "Janet's St. Regis Pecan Pie with Honey Glazed Pecans"
    #foodImg="https://spoonacular.com/recipeImages/648453-312x231.jpg"
    #foodId = 648453
    #recipeLink = 'https://spoonacular.com/janets-st-regis-pecan-pie-w-honey-glazed-pecans-648453'
    #cookTime = 45
    #servingSize = 10
    
    #ingredients = [
    #'cup firmly packed brown sugar',
    #"3 tablespoons butter.. please use real butter... don't make me come over there!",
    #'3 tablespoons melted butter',
    #'1 cup light corn syrup',
    #'4 eggs',
    #'1 cup granulated sugar',
    #'3 tablespoons honey',
    #'1 1/2 cups pecan halves',
    #'1/4 teaspoon salt',
    #'1/2 cup semisweet chocolate chips (I used minis, but any will work)',
    #"1 teaspoon vanilla(real..don't you dare use imitation!)"
    #]
    
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
        'recipeLink':recipeLink,
        'cookTime':cookTime,
        'servingSize':servingSize
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
