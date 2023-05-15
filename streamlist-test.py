import requests
import random
import streamlit as st

# Wikipedia API base URL
wiki_url = 'https://en.wikipedia.org/w/api.php'

# search - present Python final
search_term = st.text_input('Enter a search term, I will generate a random Wikipedia definition for you')

# Copy code from Youtube Video: https://www.youtube.com/watch?v=gr_KyGfO_eU
# CSS style sheet use in Streamlit
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Create a SessionState object to store persistent values
session_state = st.session_state

# Initialize search_results if it doesn't exist in session_state
if 'search_results' not in session_state:
    session_state.search_results = []

# Create a button
if st.button('Search'):
    # Wiki input: https://en.wikipedia.org/api/rest_v1/#/
    wiki_params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': search_term
    }
    response = requests.get(wiki_url, params=wiki_params)

    data = response.json()
    session_state.search_results = data['query']['search']
    
    # Select a random search result
    random_result = random.choice(session_state.search_results)
    # user input
    if session_state.search_results:
        st.markdown(
            f"<div class='search-box'><p class='userInput'>User Input: {search_term}</p></div>",
            unsafe_allow_html=True
        )

    # Remove HTML tags
    snippet_text = random_result['snippet'].replace('<span class="searchmatch">', '').replace('</span>', '')

    date_str, time_str = random_result['timestamp'].split('T')
    time_str = time_str[:-1]  # Remove Z

    # Print the desired information wrapped in a div with the class 'search-result'
    result_string = f"<div class='search-result'><p>{date_str} {time_str}</p><h2 style='font-family: InputMonoNarrow; color: white; font-size: 28px; font-style: normal;'>{random_result['title']}</h2>{snippet_text}</div>"
    st.markdown(result_string, unsafe_allow_html=True)

    # Save the result to an txt file
    #refrence from: https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file
    text_result_string = f"Date: {date_str} {time_str}\nTitle: {random_result['title']}\nSnippet: {snippet_text}"

    # Create a button
    st.download_button(
        label="Save this result !",
        data=text_result_string,
        file_name="wikipedia_search_result.txt",
        mime="text/plain"
    )