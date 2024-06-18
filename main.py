# main.py

import streamlit as st
from PIL import Image
import base64
from research_support import show_research_support_page
from admissions import show_admissions_page  # Import the admissions function

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'selected_department' not in st.session_state:
    st.session_state.selected_department = None
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'selected_sub_department' not in st.session_state:
    st.session_state.selected_sub_department = None

# Define a function to handle the login process
def login(username, password):
    if username == "Francis" and password == "password1234":
        st.session_state.logged_in = True
        st.session_state.username = username
        return True
    else:
        st.sidebar.error("Invalid username or password")
        return False

# Define the departments and their subdivisions
departments = {
    "Research Innovation and Outreach": ["Research Support", "Innovation and Incubation", "Collaborations and Partnerships"],
    "Enrollment Directorate": [],
    "Office of the Registrar": ["Admissions Office", "Examinations Office"],
    "Directorate of Alumni": [],
    "Student Affairs": [],
    "Schools": ["School of Business", "School of Technology", "School of Education", "PPTI"]
}

# Set page config for title and layout
st.set_page_config(page_title="KCA University Bureau of Statistics", layout="centered")

# Apply custom CSS for the theme
st.markdown("""
    <style>
    body {
        background-color: #001f3f;
        color: #996515;
    }
    .stApp {
        background-color: #001f3f;
    }
    .stButton>button {
        background-color: #996515;
        color: #001f3f;
        border-radius: 10px;
        font-size: 18px;
        padding: 10px 20px;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: #001f3f;
        color: #996515;
        transform: scale(1.05);
    }
    .centered-text {
        text-align: center;
        color: #996515;
    }
    .centered-logo img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .welcome-message {
        text-align: center;
        font-size: 24px;
        color: white;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to load and display a background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local('background_image.png')  # Ensure this path is correct

# Login Sidebar
def show_login_sidebar():
    logo = Image.open("kcau_logo.png")  # Ensure this path is correct
    st.sidebar.image(logo, width=150)
    st.sidebar.title("Login")
    st.sidebar.write("You are required to log in to access the KCAU Platform")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login(username, password):
            st.session_state.page = "home"

# Sidebar after login
def show_sidebar_after_login():
    st.sidebar.title("Log in Successful!")
    st.sidebar.write(f"Welcome {st.session_state.username}, please select a Division, Directorate, or Department to proceed.")

# Department Selection Page
def show_department_selection_page():
    st.markdown("<h1 class='centered-text'>KCA University Bureau of Statistics</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='centered-text'>Welcome</h2>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-message'>The KCA University Bureau of Statistics serves as a central repository for integrated, university-wide data, providing a single source of truth for all academic and administrative units. This platform aims to enhance data-driven decision-making by offering comprehensive, accurate, and timely data. By leveraging the power of data analytics, the portal empowers stakeholders to make informed decisions that drive academic excellence, operational efficiency, and strategic planning. The KCAU Data Portal is an essential tool in our commitment to transparency, accountability, and continuous improvement in the higher education landscape..</div>", unsafe_allow_html=True)

    for department in departments:
        if st.sidebar.button(department):
            st.session_state.selected_department = department
            st.session_state.page = "department_details"

# Department Details Page
def show_department_details_page():
    st.markdown(f"<h1 class='centered-text'>KCA University Bureau of Statistics - {st.session_state.selected_department}</h1>", unsafe_allow_html=True)
    subdivisions = departments[st.session_state.selected_department]
    if subdivisions:
        st.write("Directorates/Departments/Schools:")
        for subdivision in subdivisions:
            if st.button(subdivision):
                st.session_state.selected_sub_department = subdivision
                if subdivision == "Research Support":
                    st.session_state.page = "research_support"
                elif subdivision == "Admissions Office":
                    st.session_state.page = "admissions"  # Add a page for admissions
                else:
                    st.write(f"{subdivision} Page still under Development...")
    else:
        st.write("No subdivisions available")
    if st.button("Back"):
        st.session_state.page = "home"

# Main App Logic
if not st.session_state.logged_in:
    show_login_sidebar()
else:
    show_sidebar_after_login()

    if 'page' not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        show_department_selection_page()
    elif st.session_state.page == "department_details":
        show_department_details_page()
    elif st.session_state.page == "research_support":
        show_research_support_page()  # Call the function from the imported module
    elif st.session_state.page == "admissions":
        show_admissions_page()  # Call the function from the imported module
