from pathlib import Path

import streamlit as st
from PIL import Image

# Path to the folder where the images are stored
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() # Path to the current directory
css_file = curr_dir / "styles\main.css" # Path to the css file
resume_file = curr_dir / "assets\Resume-Ankit-Das-3.pdf"# Path to the resume file
profile_pic = curr_dir / "assets\profile.jpg" # Path to the profile picture

#General Settings
PAGE_TITLE = "Digital CV | Ankit Das"
PAGE_ICON = ":sunglasses:"
PAGE_THEME = "light"
PAGE_LAYOUT = "centered"
DESCRIPTION = """
I'm a student, I love every aspect of it from analysis to implementation and everything in between and in my free
time learn and experiment with SEO. with a strong proficiency in Python and its data analysis libraries
"""
PAGE_WIDTH = 1200
PAGE_HEIGHT = 1000
PAGE_INITIAL_SIDEBAR_STATE = "auto"
PAGE_INITIAL_EXPANDER_STATE = "auto"
EMAIL = "ankitdasamd@gmail.com"
PAGE_MENU_ITEMS = {
    "Home": "Home",
    "About": "About",
    "Projects": "Projects",
    "Resume": "Resume",
    "Contact": "Contact"
}
PROJECTS = {
    "Project 1": "Project 1",
    "Project 2": "Project 2",
    "Project 3": "Project 3",
}
SOCIAL_LINKS = {
    "GitHub": "https://github.com/PiKa919",
    "LinkedIn": "https://www.linkedin.com/in/ankitdas919",
    "StackOverflow": "https://github.com"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=PAGE_LAYOUT, initial_sidebar_state=PAGE_INITIAL_SIDEBAR_STATE)

st.title("Ankit Das")

#Load CSS, pdf and profile pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
with open(resume_file, "rb") as pdf_file:
    PDFbytes = pdf_file.read()
    
profile_pic = Image.open(profile_pic)


#hero SEction
col1, col2 = st.columns(2, gap="small")
with col1: 
    st.image(profile_pic, width=300)
    # st.markdown("Insert Image")
    
with col2:
    st.title("Ankit Das")
    st.write(DESCRIPTION)
    st.download_button(
        "♦ Download Resume", 
        data=PDFbytes, 
        file_name=resume_file.name, 
        mime="application/octet-stream",
        )
    st.write("Email: ", EMAIL)
    
    
    
#---SOCIAL LINKS----#
st.write("Social Links")

cols = st.columns(len(SOCIAL_LINKS))
for index, (platform, link) in enumerate(SOCIAL_LINKS.items()):
    cols[index].write(f"[{platform}]({link})") 
    
    
#---PROJECTS----#
