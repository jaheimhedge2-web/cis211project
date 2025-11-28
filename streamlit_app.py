import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Jaheim Hedge | Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', ' 💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home': 
  st.markdown('<p class="main-header">Jaheim Hedge</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring Business owner l | Medgar Evers College</p>', unsafe_allow_html=True)

# Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.2', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '10+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am a 3rd year student at Medgar Ever College majoring in Business Administration. I aspire to own multiple business
                as my goal is to be financially stable while being self employed.
            
                🎯 **Current Focus:** Graduating with Bachelors in Business Administration.
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I was born and rasied in Kingston,Jamaica
            ''')
  with col2:
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/grumpy_cat.jfif', use_column_width=True)

# About Page
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('' )
    - Major: Business Administration
                - Relevant Coursework: International Business, Human Resources
                

  with st.expander('2023 - 2025: Midwood High School):
    st.write('''
                - 'Football Player 🏈'
                - 'Carribean Fest 🇯🇲'
                
            
  st.subheader('Interests & Hobbies 🏈')
  interests = ['Sneakers 👟', 'Football 🏈', '', 'Basketball 🏀', 'Travel✈️', 'Video Games 🎮']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
  
