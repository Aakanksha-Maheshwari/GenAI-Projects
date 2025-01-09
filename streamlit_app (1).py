import streamlit as st
from streamlit import session_state as state

# Define individual pages for homework 1 and homework 2
hw6_page = st.Page("News Reporting Bot for Real-Time Content Ranking.py", title="News Reporting Bot for Real-Time Content Ranking")
hw5_page = st.Page("Course Assistant Chatbot with RAG and Vector Database.py", title="Course Assistant Chatbot with RAG and Vector Database")
hw4_page = st.Page("Course information chatbot.py", title="Course information chatbot")
hw3_page = st.Page("streaming chatbot that discusses a URL.py", title="streaming chatbot that discusses a URL")
hw2_page = st.Page("URL Summarizer for multiple LLMs.py", title="URL Summarizer for multiple LLMs")
hw1_page = st.Page("googlecolab.py", title="googlecolab")

# Initialize navigation with the pages
pg = st.navigation([hw6_page, hw5_page,hw4_page,hw3_page,hw2_page,hw1_page])

# Set page configuration (optional but helps with page title and icon)
st.set_page_config(page_title="Homework Manager", page_icon=":memo:")

# Run the navigation system
pg.run()
