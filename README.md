# This program generates a random tweet based on a food selected from a list.

# To set this up on your machine you will need to follow these steps:

>1. Sign up for a Twitter developer account and find:
>        a. API key.      
>        
>        b. API secrete key
>        
>        c. ACCESS TOKEN key
>        
>        d. ACCESS TOKEN SECRET key  
>
>    #### **(THESE ARE SECRET DO NOT SHARE WITH ANYONE)**
>                
>2. Clone this repository using git clone https://github.com/NJIT-CS490/project1-aaa237
>3. In your local copy of this repo, create a new root-level file called project1.env
>4. Add the following lines into project1.env and fill with your secret keys:
>        
>        a. export API_KEY='your_key_here'
>        
>        b. export API_SECRET_KEY='your_key_here'
>        
>        c. export ACCESS_TOKEN='your_key_here'
>            
>        d. export ACCESS_TOKEN_SECRET='your_key_here'
>                
>    #### **Do not forget to save the file and run the command: source project1.env**
>    
>5. Install tweepy by running the following, where the brackets indicate optional changes 
>    to the command you may have to run: [sudo] [/path/to/]pip[3] install tweepy
>6. Install flask using the same process as above: [sudo] [/path/to/]pip[3] install flask
>7. Run python project.py
>8. If on Cloud9, preview templates/index.html. This should successfully render the HTML!
>9. Also on Cloud9, you may pop the preview out to view in browser.


# Questions:
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
>    ## Known problems:
>            
>       a. Sometimes the tweets will not be 100% relevant to the food mentioned, 
>            one way to handle this would be to check for a certain percentage 
>            of "food-related" terms before displaying the tweet
>            
>       b. Occasionally the program will still reach the tweepy rate limit, despite handling for infinite loops.
>            This can be handled by catching the error and displaying a default tweet screen, instead of the error message
>        
>    ## Things to improve:
>            
>        a. One way this program can be improved is to allow the user to 
>            input their own list of foods to cycle through
>            
>        b. Another feature that could be implemented is to generate multiple 
>            tweets at once and display them in a list

This is a test edit