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
    st.subheader('Get to Know me 😎')
    st.write('''
                I am a 3rd year student at Medgar Ever College majoring in Business Administration. I aspire to own multiple business
                as my goal is to be financially stable while being self employed.
            
                🎯 **Current Focus:** Graduating with Bachelors in Business Administration.
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I was born and rasied in Kingston,Jamaica
            ''')
  with col2:
    # Placeholder for image
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.4qNnZ60z4uGmXKZSMQdtXgHaEo%3Fpid%3DApi&f=1&ipt=7de5e6a485ca521d94ad0dc6d9e0d24b724e3d4b8f03ff91b471643f1d6d312b&ipo=images', use_column_width=True)

# About Page
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2024 - Present: Medgar Evers College'):
    st.write('''
      - Major: Business Administration 
      - Relevant Coursework: Human Resources Management, International Business, Essentials of Marketing
       - Worked while going School         
            ''')
    

  with st.expander('2019 - 2023: Midwood High School 🏫' ):
    st.write('''
                - Played on The Football Team
                - Participated In Carribean Fest
                - Spent my Sophmore year In Jamaica due to Covid-19
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Video Games 🎮', 'Sneakers 👟', 'Football 🏈', 'Basketball 🏀', 'Travel✈️', 'The Wire 📺']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png', use_column_width = True)

    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg', use_column_width = True)
    with col2:
      st.subheader('📊 Student Grade Calulator')
      st.write('Interactive web app for calculating and visualizing grades')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** Jahgotsole2@gmail.com

        🏢 **LinkedIn:** [https://www.linkedin.com/in/jaheim-hedge-2b3428240/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BWtNU%2BRW0RTiE2dKVg9T3Lw%3D%3D](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/jaheimhedge2](https://github.com)

        📷 **Instagram:** [@Jahgotsole](https://www.instagram.com/jahgotsole)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '📺 Watching Tv',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Jaheim Hedge </center>',
        unsafe_allow_html = True
    )
    



      










