import requests
import random
import streamlit as st

# Wikipedia API base URL
wiki_url = 'https://en.wikipedia.org/w/api.php'

# search - present Python final
search_term = st.text_input('Enter a search term, I will generate a random Wikipedia definition for you')

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
    snippet_text = random_result['snippet'].replace('<span class="searchmatch">', '').replace('</span>', '')

    date_str, time_str = random_result['timestamp'].split('T')
    time_str = time_str[:-1]  # Remove Z

    # Print the desired information
    st.write(f"<p align-items: right;>{date_str} {time_str}</p>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='font-family: Helvetica, Arial, sans-serif; font-size: 48px; font-style: normal; font-variant: normal; font-weight: 700;'>{random_result['title']}</h2>", unsafe_allow_html=True)
    st.write(snippet_text)
