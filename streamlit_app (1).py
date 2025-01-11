import streamlit as st
from streamlit import session_state as state

# Define individual pages for homework 1 and homework 2
hw3_page = st.Page("Building an iSchool Chatbot with Retrieval-Augmented Generation (RAG).py", title="HW3")
hw2_page = st.Page("Multi-LLM URL Summarizer Application.py", title="HW2")
hw1_page = st.Page("News Reporting Bot for Real-Time Content Ranking.py", title="HW1")

# Initialize navigation with the pages
pg = st.navigation([hw3_page,hw2_page,hw1_page])

# Set page configuration (optional but helps with page title and icon)
st.set_page_config(page_title="Homework Manager", page_icon=":memo:")

# Run the navigation system
pg.run()