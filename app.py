import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Header
st.title("👋 Hi, I'm Shamanth")
st.subheader("Ai Engineer | Data scientist | Data Analyst")

# About Me
st.header("About Me")
st.write("""
I'm passionate about data science, machine learning, data analysis and frontend  development(I do development for fun).  
This portfolio showcases my projects, skills, and experience.
""")

# Skills
st.header("Skills")

skills = {
    "Programming Languages": ["Python", "Java", "JavaScript", "SQL", "PHP"],
    "Web Development": ["React", "HTML/CSS", "Flask", "Apache"],
    "Data Science & ML": [
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing (NLP)",
        "Computer Vision",
        "AI/ML Engineering",
        "Exploratory Data Analysis (EDA)"
    ],
    "Data Tools": ["Pandas", "NumPy", "Excel", "Tableau", "Power BI", "Data Visualization"],
    "DevOps & Others": ["Git/GitHub", "Streamlit", "Docker", "n8n"]
}

for category, items in skills.items():
    st.subheader(category)
    st.write(", ".join(items))


# Projects
st.header("Projects")

with st.expander("🌳 Decision Tree  Analysis"):
    st.write("""Implemented a classification model using **Decision Trees** and **CHAID (Chi-squared Automatic Interaction Detector)** 
    to analyze categorical data and identify key decision rules.  
    Compared performance with standard decision tree algorithms and visualized tree splits for better interpretability.
    """)
    st.markdown("[GitHub Repo](https://github.com/Shamanth-8/ml/blob/main/decision%20tree%20and%20chaid.ipynb)")


with st.expander("🤖 Fraud Detection with Autoencoders and deep neural network"):
    st.write("Built a fraud detection model using autoencoders, evaluated with precision, recall, F1, AUC-ROC.")
    st.markdown("[GitHub Repo](https://github.com/Shamanth-8/hsbc-hackathon-data-science-/blob/main/hsbchackathon.ipynb)")


with st.expander("🛠️ Code Pilot – AI Coding Assistant"):
    st.write("""
    Developed an AI-powered coding assistant that helps analyze, debug, and generate code snippets.  
    Integrated natural language prompts with backend logic to provide real-time programming support 
    for Python and other languages.
    """)
    st.markdown("[GitHub Repo](https://github.com/Shamanth-8/rabbitai)")
    st.markdown("[Live Demo](https://rabbitai-1.onrender.com/)")


# Contact
st.header("Contact")
st.write("📧 Email: theshampatel@gmail.com")
st.write("🌐 LinkedIn: www.linkedin.com/in/shamanth-patel-78a091233")
st.write("🐙 GitHub: https://github.com/Shamanth-8")
