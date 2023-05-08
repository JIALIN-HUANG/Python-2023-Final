import requests
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
    st.write(data['query']['search'][0])