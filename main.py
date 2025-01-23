import streamlit as st
from parse import parse_with_ollama
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
st.title("AI WEB SCRAPER APP")
url = st.text_input("Enter your URL here:")

if st.button("Scrape URL"):
    st.write("Scraping URL...") 

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("Display content"):
        st.text_area("DOM CONTENT", cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what do you want to search for?")

    if st.button("Search"):
        if parse_description:
            st.write("Searching for content...") 

            dom_chunks = split_dom_content(st.session_state.dom_content)
            results = parse_with_ollama(dom_chunks, parse_description)
            st.write(results)