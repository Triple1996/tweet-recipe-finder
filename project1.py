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
    
    #spoonacularRes = requests.get('https://api.spoonacular.com/food/products/search?query='+randFood+'&apiKey='+api_key+'&number=5')
    
    # query spoonacular recipes
    ##spoonacularRes = requests.get('https://api.spoonacular.com/recipes/complexSearch?query='+randFood+'&apiKey='+api_key+'&number=5')
    ##foodsList = spoonacularRes.json()
    ##print(foodsList)
    ##food = random.choice(foodsList['results'])
    food = random.choice([
        {'id': 651225, 'title': 'Mashed Potatoes with Garlic, Sage & Goat Cheese', 'image': 'https://spoonacular.com/recipeImages/651225-312x231.jpg', 'imageType': 'jpg'}, 
        {'id': 640659, 'title': 'Creamy Mashed Potatoes', 'image': 'https://spoonacular.com/recipeImages/640659-312x231.jpg', 'imageType': 'jpg'}, 
        {'id': 640661, 'title': 'Creamy Mashed Potatoes with Parsley', 'image': 'https://spoonacular.com/recipeImages/640661-312x231.jpg', 'imageType': 'jpg'}, 
        {'id': 1022743, 'title': 'The Best Mashed Potatoes', 'image': 'https://spoonacular.com/recipeImages/1022743-312x231.jpg', 'imageType': 'jpg'}, 
        {'id': 654679, 'title': 'Parmesan Mashed Potatoes', 'image': 'https://spoonacular.com/recipeImages/654679-312x231.jpg', 'imageType': 'jpg'}])
    foodTitle = food['title']
    foodImg = food['image']
    foodId = food['id']
    #foodTitle = "Mashed Potatoes"
    #foodImg = "https://spoonacular.com/recipeImages/654679-312x231.jpg"
    
    
    
    # get recipe info using id
    ##recipe = requests.get('https://api.spoonacular.com/recipes/'+foodId+'/information?apiKey='+api_key)
    
    ##print(recipe.json()['extendedIngredients'])
    ##ingredientsAmounts = []
    spoonRes =   [
        {
            'id': 14121,'aisle': 'Beverages','image': 'sparkling-water.png','consistency': 'liquid', 
            'name': 'club soda','original': '1/4 cup club soda','originalString': '1/4 cup club soda', 
            'originalName': 'club soda', 'amount': 0.25, 'unit': 'cup','meta': [],'metaInformation': [],
            'measures':{ 'us': {'amount': 0.25, 'unitShort': 'cups', 'unitLong': 'cups'}, 
            'metric': {'amount': 59.147, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, 
        {'id': 2064, 'aisle': 'Produce', 'image': 'mint.jpg', 'consistency': 'solid', 'name': 'fresh mint', 'original': '1 tablespoon fresh mint', 'originalString': '1 tablespoon fresh mint', 'originalName': 'fresh mint', 'amount': 1.0, 'unit': 'tablespoon', 'meta': ['fresh'], 'metaInformation': ['fresh'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}, 'metric': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}}}, 
        {'id': 9160, 'aisle': 'Produce', 'image': 'lime-juice.png', 'consistency': 'liquid', 'name': 'lime juice', 'original': '1 tablespoon lime juice', 'originalString': '1 tablespoon lime juice', 'originalName': 'lime juice', 'amount': 1.0, 'unit': 'tablespoon', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}, 'metric': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}}}, 
        {'id': 14037, 'aisle': 'Alcoholic Beverages', 'image': 'rum-dark.jpg', 'consistency': 'liquid', 'name': 'rum', 'original': '1 ounce rum', 'originalString': '1 ounce rum', 'originalName': 'rum', 'amount': 1.0, 'unit': 'ounce', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'oz', 'unitLong': 'ounce'}, 'metric': {'amount': 28.35, 'unitShort': 'g', 'unitLong': 'grams'}}}, 
    ]
    
    ingredientsAmounts = []
    ##for ingredient in recipe.json()['extendedIngredients']:
    ##    ingredientsAmounts.append(ingredient['originalString'])
    for ingredient in spoonRes:
        ingredientsAmounts.append(ingredient['originalString'])
    
    # params dict
    d = {
        'tweet':tweetText,
        'food':randFood,
        'author':tweetAuthor,
        'date':tweetDate,
        'foodTitle':foodTitle,
        'foodImg':foodImg,
        'len':len(ingredientsAmounts),
        'ingredients':ingredientsAmounts
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
