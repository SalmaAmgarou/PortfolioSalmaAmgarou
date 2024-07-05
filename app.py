from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# --Path Setting--
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv_salma_amgarou.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---General Setting ---#
EMAIL = "salma.amgarou@etu.uae.ac.ma"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/salma-amgarou-577741276/",
    "GitHub": "https://github.com/SalmaAmgarou",
    "Facebook": "https://www.facebook.com/yourfacebook",
    "Twitter": "https://twitter.com/yourtwitter"
}

st.set_page_config(
    page_title="Salma Amgarou🧊",
    page_icon=":computer:",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Apply the custom CSS
local_css(css_file)

# Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.


# Background and styling using CSS
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-color: #343434;
             color: white;
             font-family: 'Arial', sans-serif;
         }}
         .stApp p {{
             text-align: justify;
         }}
         h1,h2 {{
             color: #e040fb;
         }}
         h3, h4, h5, h6{{
            color: white;
         }}
         a {{
             color: #e040fb;
         }}
         .stButton>button {{
             background-color: #e040fb;
             color: white;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

# --- INTRO ---
# Profile pic and Resume
with open(resume_file, "rb") as pdf_file:
    PDF_Byte = pdf_file.read()
pro_pic = Image.open(profile_pic)
with st.container():
    col1, col2 = st.columns((2, 2))

    with col1:
        st.image(pro_pic, width=400)

    with col2:
        st.write("Click Below to download the file :point_down: ")
        st.download_button(
            label="Download Resume :page_facing_up:",
            data=PDF_Byte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write(":email:", EMAIL)

with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Portfolio!")
        st.subheader("Hi, I am Salma Amgarou :desktop_computer:")
        st.subheader(
            """
            I am a *Data Scientist* specializing in *Artificial Intelligence* and *Data Science*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            Passionate about AI and technology, with solid programming expertise.
            My journey has allowed me to develop sharp skills in Data Science, Machine Learning, and AI.
            I'm determined to put these skills into practice in a professional environment.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json"),
            height=300,
        )

# --- Education ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uqsv3ztj.json"),
            height=300,
        )
    with col2:
        st.header("Education")
        st.subheader(
            """
             	 Faculty of Sciences and Techniques of Tangier (FSTT) \n
             	:round_pushpin: Tangier, Morocco \n 
             	:calendar: 2023 - Present \n
             	 Master's in Artificial Intelligence and Data Science \n
            """
        )
        st.subheader(
            """
                 Faculty of Sciences and Techniques of Tangier (FSTT) \n
                :round_pushpin: Tangier, Morocco \n
                :calendar: 2022 - 2023 \n
                 Bachelor's in Computer Engineering \n
            """
        )

# --- Work Experience---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st_lottie(
            load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json"),
            height=300,
        )
    with col1:
        st.header("Work Experience")
        st.subheader(
            """
                💼 Algorithmics School \n
                :bookmark_tabs: Computer Science Educator \n 
                :calendar: November 2023 - Present \n
                :pushpin: | Teaching | Python | Scratch | Java | Front-End Development |
                Simplified technical concepts for diverse audiences and effectively communicated complex ideas. \n
            """
        )
        st.subheader(
            """
                 💼 Sanford Federal Inc. \n
                :bookmark_tabs: IT Support / IT Technician Intern\n
                :calendar: July 2023 - September 2023 \n
                :pushpin: | Hardware/Software Installation | User Administration | Windows Server 2019 | Azure AD |
                Managed IT service requests and supported web development projects. \n
            """
        )
        st.subheader(
            """
                 💼 ISPITS Tangier \n
                :bookmark_tabs: Web Solution Developer Intern \n
                :calendar: April 2023 - June 2023 \n
                :pushpin: | Web Development | WordPress | PHP | HTML | JavaScript | CSS |
                Developed a website and web application for a university, including custom WordPress theme. \n
            """
        )

# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages & Frameworks
            - Python, Java, Scala, C, C++, JavaScript, HTML5, CSS, Bootstrap, PHP, jQuery
            Databases
            - MySQL, NoSQL, TSQL
            Machine Learning & AI
            - Supervised/Unsupervised Machine Learning, Deep Learning (CNN, RNN), NLP (LLM), ChatBot Development
            Data Science & Big Data
            - Data Mining, Data Analysis, Power BI, Hadoop, Spark (PySpark), Yarn, HBase, Hive & Sqoop, Kafka
            IoT & Networking
            - Arduino, Raspberry Pi, Mosquitto, Packet Tracer Simulation, Node-RED
            Other
            - Web Scraping (Scrapy Spider, BeautifulSoup, Selenium), LAMP & WAMP Stack, CMS WordPress, LMS Moodle
             """
        )

    with col1:
        st_lottie(
            load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lln7m43m.json"),
            height=300,
        )

# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.subheader("Take a look at some of my works!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "https://cdn.futura-sciences.com/sources/images/2-cancer.jpeg")
        st.subheader("Cancer Classification Project")
        st.write(
            "Developed a machine learning model to classify ovarian or prostate cancer types using Extreme Gradient Boosting & Naive Bayes from scratch.")

    with col2:
        st.image(
            "https://cdn.thenewstack.io/media/2021/11/28de6660-screen-shot-2021-11-29-at-6.46.11-am.png")
        st.subheader("Streamlit Machine Learning App")
        st.write(
            "Developed a versatile Low-code/No-Code application in Python facilitating the Machine Learning process from data preprocessing to model training.")
        if st.button('Github', key="ml_app_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/SalmaAmgarou/AutoML-WebApp.git)'  # Replace with actual link
            st.markdown(link, unsafe_allow_html=True)
    with col3:
        st.image(
            "https://www.nesi.org.nz/sites/default/files/styles/case_study_large/public/CelineCattoenGilbert-NeSICaseStudy-heroimage.png?itok=PT5Z447i")
        st.subheader("River Depletion Forecasting in Morocco")
        st.write(
            "Developed a Python application for analyzing qualitative and quantitative data using various machine learning algorithms such as linear regression, decision trees, and neural networks.")
        if st.button('Github', key="river_prediction_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/SalmaAmgarou/RiversMorocco.git)'  # Replace with actual link
            st.markdown(link, unsafe_allow_html=True)

with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(
            "data:image/jpeg;base64,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")
        st.subheader("FSTT Chatbot")
        st.write(
            "Developed a chatbot in French and Arabic for FSTT, using advanced natural language processing techniques such as Research Augmented Generation (RAG) and vector databases.")
        if st.button('Github', key="chatbot_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/SalmaAmgarou/FSTT-ChatBot.git)'  # Replace with actual link
            st.markdown(link, unsafe_allow_html=True)
    with col5:
        st.image(
            "https://images.frandroid.com/wp-content/uploads/2022/11/twitter-alexander-shatov-scaled.jpg")
        st.subheader("Big Data Twitter Sentiment Analysis Project")
        st.write(
            "Utilized Hadoop, Spark, and other big data technologies to analyze large datasets and extract meaningful insights.")
        if st.button('Github', key="bigdata_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/SalmaAmgarou/Twitter_Sentiment_Analysis.git)'  # Replace with actual link
            st.markdown(link, unsafe_allow_html=True)
    with col6:
        st.image(
            "https://www.infofort.pt/wp-content/uploads/2023/08/smart-home-automation.jpg")
        st.subheader("IoT Smart Home System")
        st.write(
            "Developed an IoT-based smart home system using Arduino, Raspberry Pi, and MQTT protocol for efficient device communication and control.")
        if st.button('Github', key="iot_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/yourgithub/iot-smart-home)'  # Replace with actual link
            st.markdown(link, unsafe_allow_html=True)

# SOCIAL network
with st.container():
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    with col3:
        st.image(
            "https://www.freeiconspng.com/uploads/facebook-logo-new-8.png", width=100)
    with col2:
        st.image(
            "https://www.freeiconspng.com/uploads/git-github-hub-icon-25.png", width=100)
    with col1:
        st.image(
            "https://www.freeiconspng.com/uploads/linkedin-linkedin-icon-flat-icon-linkedin-png-social-icon-png-11.png",
            width=100)
    with col4:
        st.image(
            "https://www.freeiconspng.com/uploads/twitter-icon-9.png", width=100)

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Contact me details
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>CONTACT ME</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>I'd Love To Hear From You</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "https://www.freeiconspng.com/uploads/red-location-map-pin-icon-5.png", width=100)
        st.subheader("Where To Find Me!")
        st.write("Tangier, Morocco")
    with col2:
        st.image(
            "https://www.freeiconspng.com/uploads/-email-letter-mail-send-sign-icon--iconfinder-20.png", width=100)
        st.subheader("Email Me At")
        st.write("salma.amgarou@etu.uae.ac.ma")

    with col3:
        st.image(
            "https://www.freeiconspng.com/uploads/mobile-phone-icon-from-colorful-stickers-part-4-set--256x256-px-13.png",
            width=100)
        st.subheader("Call Me At")
        st.write("Phone: (+212) 608516864")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Feedback</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/salma.amgarou@etu.uae.ac.ma" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required = True>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
    for i in range(8):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            SALMA AMGAROU © 2024
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2024 with ❤, 🐍 and Streamlit</p>", unsafe_allow_html=True)
    st.write("---")
