# This program generates a random tweet based on a food selected from a list.

# To set this up on your machine you will need to follow these steps:

>1. Sign up for a Twitter developer account at: https://developer.twitter.com
>2. Navigate to the developer portal and make a new app. Click the key symbol to find: 
>
>        a. API key (KEY)
>        
>        b. API secret key (KEY_SECRET)
>        
>        c. ACCESS TOKEN key (TOKEN)
>        
>        d. ACCESS TOKEN SECRET key (TOKEN_SECRET)
>
>    #### **(THESE ARE SECRET DO NOT SHARE WITH ANYONE)**
>
>3. Sign up for a Spoonacular API account, confirm your email and copy your API_KEY
>4. Clone this repository using git clone https://github.com/NJIT-CS490/project1-aaa237
>5. In your local copy of this repo, create a new root-level file called project1.env
>6. Add the following lines into project1.env and fill with your secret keys:
>        
>        a. export KEY='your_key_here'
>        
>        b. export KEY_SECRET='your_key_here'
>        
>        c. export TOKEN='your_key_here'
>            
>        d. export TOKEN_SECRET='your_key_here'
>
>        e. export API_KEY='your_key_here'
>                
>    #### **Do not forget to save the file**
>    
>7. Install tweepy by running the following, where the brackets indicate optional changes 
>    to the command you may have to run: [sudo] [/path/to/]pip[3] install tweepy
>8. Install flask using the same process as above: [sudo] [/path/to/]pip[3] install flask
>8. Install python-dotenv using the same process as above: [sudo] [/path/to/]pip[3] install python-dotenv
>10. If running on Cloud9, that's it! Run python project.py
>11. If on Cloud9, preview templates/index.html. This should successfully render the HTML!
>12. Also on Cloud9, you may pop the preview out to view in browser.
>13. If you want to deploy this app onto Heroku, you must first register for an account at: https://signup.heroku.com/login
>14. Install heroku by running npm install -g heroku
>15. Run the following lines:
>        
>         a. heroku login -i
>
>         b. heroku create
> 
>         c. git push heroku master
>
>16. Navigate to your new heroku site
>17. Add your secret keys (from project1.env) by going to https://dashboard.heroku.com/apps and clicking on your app.
>     Click on settings, scroll down to "Config Vars", click "reveal config vars" and add each key:value pair.
>     The config var names should be:
> 
>         KEY
>
>         KEY_SECRET
>
>         TOKEN
>
>         TOKEN_SECRET
>
>18. Configure requirements.txt with all requirements needed to run your app (For this repo it is already filled in)
>19. Configure Procfile with the command needed to run your app (For this repo it is already filled in)
>20. To debug, you can use heroku log --tail


# Questions:
> 
> 
>    ## Three technical issues I encountered:
>            
>        a. Encountered a sporadic list index out of bounds error when 
>            randomly selecting a tweet. Solved by first ensuring that  
>            the random number is less than the size of result list. 
>            Later changed to using random.choice(list) for conciseness.
>        
>        b. At first many tweets being pulled were in multiple languages, 
>            making the screen unreadable. After passing the lang='en' 
>            parameter to api.search(), all tweets returned were in English
>        
>        c. After a couple page loads, I would encounter the following error: 
>        
>            tweepy.error.RateLimitError: [{'message': 'Rate limit exceeded', 'code': 88}]
>        
>            Fixed the issue by lowering the number of tweets requested, 
>            and changing the search query in the case that search() returned empty the first time.
>
>        d. Sometimes, depending on the size of the ingredients list, some text elements appeared 
>            on top of the image or out of its respective HTML wrapper. This was solved by adding
>            relative sizes and padding to certain divs, and making use of min/max sizes for height
>            and width
>        
>    ## Known problems:
>            
>       a. Sometimes the tweets will not be 100% relevant to the food mentioned, 
>            one way to handle this would be to check for a certain percentage 
>            of "food-related" terms before displaying the tweet
>            
>       b. Some HTML elements still do not survive resizing the window, and may appear 
>            jumbled up or on top of one another
>        
>    ## Things to improve:
>            
>        a. One way this program can be improved is to allow the user to 
>            input their own list of foods to cycle through
>            
>        b. One improvement to be made would be returning multiple recipes 
>            and tweets in one page load, so the user could navigate through
>            a selection of recipes and choose one or a few that they like
