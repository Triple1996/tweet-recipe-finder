This program generates a random tweet based on a food selected from a list.

To set this up on your machine you will need to follow these steps:

1. Sign up for a Twitter developer account and find:
2. 
        a. API key.      

        b. API secrete key
        
        c. ACCESS TOKEN key
        
        d. ACCESS TOKEN SECRET key  (THESE ARE SECRET DO NOT SHARE WITH ANYONE)
        
2. Clone this repository using git clone
3. In your local copy of this repo, create a new root-level file called project1.env
4. Add the follwing lines into project1.env
5. 
        a. export API_KEY='your_key_here'

        b. export API_SECRET_KEY='your_key_here'
        
        c. export ACCESS_TOKEN='your_key_here'
    
        d. export ACCESS_TOKEN_SECRET='your_key_here'
        
    Do not forget to save the file and run the command: source project1.env
    
5. run the following, where the brackets indicate optional changes to the command you may have to run:
    [sudo] [/path/to/]pip[3] install tweepy


Questions:

    Three technical issues I encountered:
    
        a. Encountered a sporadic list index out of bounds error when randomly selecting a tweet. 
            Solved by first ensuring that the random number is less than the size of result list. Later changed to using random.choice(list) for conciseness.
        
        b. At first many tweets being pulled were in multiple languages, making the screen unreadable. After passing the lang='en' parameter to api.search(), 
            all tweets returned were in English
        
        c. 
        
    Known problems:
    
        Sometimes the tweets will not be 100% relevant to the food mentioned
        
    Things to improve:
    
        a. One way this program can be improved is to allow the user to input their own list of foods to cycle through
        b. Another feature that could be implemented is to generate multiple tweets at once and display them in a list