import requests
from bs4 import BeautifulSoup
import random
import streamlit as st

# Wikipedia API base URL
wiki_url = 'https://en.wikipedia.org/w/api.php'

# search - present Python final
search_term = st.text_input('Enter a search term', 'Python Final')

# Create a button
if st.button('Search Wikipedia'):
    # Wiki input: https://en.wikipedia.org/api/rest_v1/#/
    wiki_params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': search_term
    }

    # Query the Wikipedia API and get the response
    response = requests.get(wiki_url, params=wiki_params)

    data = response.json()
    search_results = data['query']['search']
    
    # Select a random search result
    random_result = random.choice(search_results)

    # Remove HTML tags from the snippet
    soup = BeautifulSoup(random_result['snippet'], 'html.parser')
    snippet_text = soup.get_text()

    # Print the desired information
    st.write('Title:', random_result['title'])
    st.write('Snippet:', snippet_text)
    st.write('Timestamp:', random_result['timestamp'])