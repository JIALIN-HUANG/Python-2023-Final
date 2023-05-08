import requests
import streamlit as st
import tweepy

# Set up API keys and access tokens for Twitter
TWITTER_API_KEY = 'ZIRswi403CUWgby0MGYBj6X7r'
TWITTER_API_SECRET = 'ABzoiLlTmjXiXkiW5mLAytNAD6WGaQ3mJW2APhmQ4PvLmyPju7'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACd3iQEAAAAA42jdPCLcyphYR%2FJRa8UUBMo7pdY%3DkcQ0zV7gftfWPZn7rptsTzBTTQHmNueTX7kxLo8N4r3tvFtQpl'

# Authenticate with Tweepy
auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
api = tweepy.API(auth)

# Wikipedia API base URL
wiki_url = 'https://en.wikipedia.org/w/api.php'

# Create input fields for search term
search_term = st.text_input('Enter a search term', 'Python')

# Create a button to submit the form
if st.button('Search Wikipedia'):
    # Build the Wikipedia API URL with user input
    wiki_params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': search_term
    }

    # Query the Wikipedia API and get the response
    response = requests.get(wiki_url, params=wiki_params)

    # Parse the JSON response
    data = response.json()

    # Display the Wikipedia search results
    st.write(f'Wikipedia search results for "{search_term}":')
    for item in data['query']['search']:
        st.write(f'- [{item["title"]}](https://en.wikipedia.org/wiki/{item["title"].replace(" ", "_")})')

# Create a button to search for tweets containing the search term
if st.button('Search Twitter'):
    # Query the Twitter API and get the response
    tweets = api.search_tweets(q=search_term, lang='en', count=2)

    # Display the tweets containing the search term
    st.write(f'Tweets containing "{search_term}":')
    for tweet in tweets:
        user_name = tweet.user.screen_name
        tweet_text = tweet.text
        st.write(f'- @{user_name}: {tweet_text}')
