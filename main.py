import streamlit as st


# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About","Projects", "Contact"])

st.markdown(
    """
    <style>
    /* Set default font color for the entire app */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #3b82f6;
        color: white!important;
    }
    section[data-testid="stSidebar"] {
            background-color:#93c5fd;
        }
    section[data-testid="stSidebar"] * {
            color: black;
        }
    div.stDownloadButton > button {
    background-color: #336699;
    color: white!important;
    font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True) #a8a29e

if page == "Home":
    with st.container():
        col1, col2 = st.columns([1, 3]) # Adjust column ratios as needed
        with col1:
            st.markdown(
        """
        <style>
        .center-container {
            display: flex;
            height: 50px; /* Change height as needed */
            align-items: center; /* Vertical center */
            justify-content: center; /* Horizontal center */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
            # image = Image.open("insiapic.jpg")
            # st.image(image, width=200,)
            
            st.markdown('<div class="center-container">', unsafe_allow_html=True)
            st.image("insiapic.jpg")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("## 👋Hi,I'm Insia Murtaza")
            st.write("### A Passionate Learner, Webdeveloper and data enthusiast ")
            st.write("#### Welcome to my portfolio website built using Streamlit🙂")

    
if page == "About":
    st.header("About Me")
    st.write("""
    I’m a software developer with a passion for building data apps, websites, and solving real-world problems. I am working on the following:
    - ✅ Typescript
    - ✅ React,Next Js
    - ✅ Html,Css,Tailwind Css         
    - ✅ Python
    - ✅ OpenAI-SDK Agents         
    - 🎯 Interested in exploring above skills and seeking for an opportunity to work in a healthy environment where I can grow my skills simultaneously utilize them in company's growth.
    """)
    with open("my_resume.pdf", "rb") as file:
        st.download_button("Download My Resume", file, "my_resume.pdf")

if page == "Projects":

    st.header("Projects")
    st.subheader("🔹 Project 1: ")

    video_col, text_col = st.columns((1,2))
    with video_col:
        st.video("Static Interactive Resume - Personal - Microsoft​ Edge 2024-11-27 17-19-59.mp4")
    with text_col:
        st.write("A Static Interactive Resume designed using Html Css.(https://hackathon-milestonesv.vercel.app/)")

    st.subheader("🔹 Project 2: ")
    video_col, text_col = st.columns((1,2))
    with video_col:
        st.video("Create Next App - Personal - Microsoft​ Edge 2025-01-29 00-51-08.mp4")
    with text_col:
        st.write("An E-commerce website of garments developed on Next Js,React and Tailwind Css.(https://hackathon-template5.vercel.app/)")
    st.subheader("🔹 Project 3: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Governor Initiative and 3 more pages - Personal - Microsoft​ Edge 2025-06-20 18-18-44.mp4")
    with text_col:
        st.write("This project was our assignment in GIAIC program in Quarter2. It is the homepage of GovernorSindh official website developed using React,Next Js and Tailwind Css.(https://governorhouse-website.vercel.app/)")
    st.subheader("🔹 Project 4: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Streamlit - Unit Converter 2025-03-04.mp4")
    with text_col:
        st.write("This project was our first assignment in GIAIC program in Quarter3. This is a simple Unit Converter application developed in Python, featuring a user-friendly interface, and deployed it on Streamlit for web access.(https://unit-converter-insiamurtaza.streamlit.app/)")
    st.subheader("🔹 Project 5: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Streamlit Library Manager 2025-05-05.mp4")
    with text_col:
        st.write("This project was one of the assignments given in GIAIC program in Quarter3. This Library Manager can add, delete and search books by author name or title of the book. It is my personal library manager that also tells the statistics how many books are read and how many not.(https://library-manager-app-ukyqgojzozum2bedp8vdeh.streamlit.app/)")
    st.subheader("🔹 Project 6: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Streamlit Growth Mindset App- Microsoft​ Edge 2025-08-06 13-32-48.mp4")
    with text_col:
        st.write("This project was one of the assignments given in GIAIC program in Quarter3.This application developed and deployed on streamlit using Python tells the growth mindset level of the user by self assessment.(https://growth-mindset-app-5n6gybesfnmrus4ty2fdx5.streamlit.app/) ")
    st.subheader("🔹 Project 7: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Password Strength Checker · Streamlit and 1 more page - Personal - Microsoft​ Edge 2025-08-06 13-29-20.mp4")
    with text_col:
        st.write("This project was one of the assignments given in GIAIC program in Quarter3. This application asks to enter a password, checks it and guides the user to improve the password.(https://password-strength-checker-getpjjnmrsss3kp3wfxbf2.streamlit.app/) ")
    st.subheader("🔹 Project 8: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Streamlit BMI Calculator - 2025-08-08.mp4")
    with text_col:
        st.write("This project was one of the assignments given in GIAIC program in Quarter3. This application asks user to enter height and weight and calculates his/her BMI, it also gives options of units in which user can enter height and weight.(https://bmi-calculator-suagv8qdowvpdpm4cdkng2.streamlit.app/) ")
    st.subheader("🔹 Project 9: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("🔐 SecureVault · Streamlit Data Encryption App 2025-08-08.mp4")
    with text_col:
        st.write("This project was one of the assignments given in GIAIC program in Quarter3. This application asks user to first login,if user id exists and if not then asks usre to register first then login to store or retrieve data with the help of passkey.(https://data-encryption-app-cs3wkmoqer7rgrwgbwmxgn.streamlit.app/)")
    st.subheader("🔹 Project 10: ")
    video_col,text_col = st.columns((1,2))
    with video_col:
        st.video("Streamlit My-First-AI-Assistant 2025-06-25.mp4")
    with text_col:
        st.write("This project was my first assignment in Quarter4. This is an AI chatbot using Gemini api key and model.Front end GUI supported by streamlit and deployed on same. (https://myfirst-ai-agent-s7xg5trt7ctfchdzqel9uz.streamlit.app/)")
if page == "Contact":
    st.header("📫 Contact Me")
    st.write("Email: insia.mu@email.com")
    st.write("LinkedIn: (www.linkedin.com/in/insia-murtaza-7b95a6a8)")

 
