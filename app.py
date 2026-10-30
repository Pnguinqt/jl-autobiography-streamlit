import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(
    page_title="John Lawrence Dioquino | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("""
<style>
    .main { background-color: #f7f9fc; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; }
    .hero {
        padding: 2rem;
        border-radius: 18px;
        background: linear-gradient(120deg, #102a43, #256d85);
        color: white;
        margin-bottom: 1.2rem;
    }
    .hero h1, .hero p { color: white; }
    .project-card {
        border: 1px solid rgba(120,130,150,.25);
        border-radius: 14px;
        padding: 1rem 1.1rem;
        min-height: 210px;
        background: rgba(128,128,128,.04);
    }
    .small-note { color: #718096; font-size: .9rem; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("👋 Welcome")
    st.write("**John Lawrence Dioquino**")
    st.caption("BS Information Technology | 4th Year")
    st.divider()
    page = st.radio(
        "Navigate",
        ["Home", "Autobiography", "Skills", "Projects", "Contact"],
        index=0,
    )
    st.divider()
   
# Header / hero
st.markdown("""
<div class="hero">
    <p style="letter-spacing:2px; text-transform:uppercase; margin-bottom:5px;">
        Information Technology Student · Developer
    </p>
    <h1 style="font-size:2.7rem; margin:0;">John Lawrence Dioquino</h1>
    <p style="font-size:1.1rem; margin-top:10px;">
        Building practical software solutions through backend development,
        web technologies, and applied AI.
    </p>
</div>
""", unsafe_allow_html=True)

if page == "Home":
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.subheader("About Me")
        
        try:
            st.image("waragud.jpg", caption="John Lawrence Dioquino", use_container_width=True)
        except Exception:
            st.image(
                "https://placehold.co/600x600/dae6ef/17324d?text=JL",
                use_container_width=True,
            )
        st.info("Cebu Institute of Technology–University")
    with right:
        st.subheader("A little introduction")
        st.write(
            "Hello! I'm John Lawrence Dioquino, a fourth-year Bachelor of Science "
            "in Information Technology student at Cebu Institute of Technology–University. "
            "I enjoy learning how software works behind the scenes and turning ideas "
            "into useful applications. My interests include backend development, "
            "database management, web development, and AI-powered applications."
        )
        st.write(
            "I am continuously improving my programming and problem-solving skills "
            "through academic projects and independent practice. My long-term goal "
            "is to become a software developer and contribute to applications that "
            "solve real-world problems."
        )
        c1, c2, c3 = st.columns(3)
        c1.metric("Program", "BSIT")
        c2.metric("Academic Level", "4th Year")
        c3.metric("Expected Graduation", "June 2027")
        st.markdown("**Currently interested in:**")
        interests = st.multiselect(
            "Choose the topics you are interested in",
            ["Backend Development", "Artificial Intelligence", "Web Development",
             "Databases", "Software Engineering", "Badminton", "Anime"],
            default=["Backend Development", "Artificial Intelligence", "Web Development"],
        )
        st.caption("My interests: " + (", ".join(interests) if interests else "Not selected yet."))

    st.divider()
    st.subheader("Explore my portfolio")
    a, b, c = st.columns(3)
    a.markdown("### 📖 Autobiography\nRead about my background, education, interests, and milestones.")
    b.markdown("### 🧠 Skills\nExplore the technologies and skills I am developing.")
    c.markdown("### 💻 Projects\nSee selected academic and personal development work.")
   

elif page == "Autobiography":
    st.header("My Autobiography")
    st.write(
        "My journey in technology has been shaped by curiosity, practice, and the "
        "opportunity to build applications as part of my studies. As an IT student, "
        "I have learned that software development is not only about writing code; "
        "it also involves understanding users, organizing information, solving "
        "problems, and continuously improving a solution."
    )
    tab1, tab2, tab3 = st.tabs(["Background", "Education", "Interests & Milestones"])
    with tab1:
        st.subheader("Background")
        st.write(
            "I am interested in technology because it provides ways to solve everyday "
            "problems and make information more accessible. I enjoy exploring how "
            "applications communicate with databases and how different parts of a "
            "system work together."
        )
    with tab2:
        st.subheader("Education")
        st.markdown("""
        **Cebu Institute of Technology–University**  
        Bachelor of Science in Information Technology  
        Fourth Year · Expected graduation: June 2027

        **Certification:**  
        - ICT NC II
        """)
    with tab3:
        st.subheader("Interests")
        st.write(
            "Outside programming, I enjoy watching anime and playing badminton. "
            "I also like exploring new tools and technologies that can help me "
            "become a better developer."
        )
        st.subheader("Milestones")
        timeline = [
            ("Academic foundation", "Started building knowledge in programming, databases, and systems development."),
            ("ICT NC II", "Earned an ICT NC II certification."),
            ("DugoSugbo", "Developed an individual blood stock management system as an academic project."),
            ("ALLY", "Worked primarily on backend development for an AI-powered Philippine legal assistant capstone."),
            ("Current focus", "Continuing to strengthen software development and AI-related skills."),
        ]
        for heading, detail in timeline:
            with st.expander(heading):
                st.write(detail)

elif page == "Skills":
    st.header("Technical Skills")
    st.write(
        "The ratings below are editable self-assessments for presentation purposes. "
        "Adjust them to reflect your actual confidence and experience before submitting."
    )
    skill_data = {
        "Skill": ["Java", "Spring Boot", "Python", "ReactJS", "MySQL", "REST API", "Git/GitHub"],
        "Self-rating (1–5)": [3, 3, 3, 2, 3, 3, 3],
        "Area": ["Programming", "Backend", "Programming", "Frontend", "Database", "Backend", "Tools"],
    }
    skills_df = pd.DataFrame(skill_data)
    st.dataframe(skills_df, use_container_width=True, hide_index=True)
    selected_skill = st.selectbox("Choose a skill to review", skills_df["Skill"].tolist())
    current_rating = int(skills_df.loc[skills_df["Skill"] == selected_skill, "Self-rating (1–5)"].iloc[0])
    st.write(f"**{selected_skill}** — current self-rating: {current_rating}/5")
    new_rating = st.slider("Adjust your rating", min_value=1, max_value=5, value=current_rating)
    st.caption(f"Your selected rating for {selected_skill}: {new_rating}/5")

    st.subheader("Skill rating chart")
    st.bar_chart(skills_df.set_index("Skill")["Self-rating (1–5)"])
    st.caption("Scale: 1 = beginner, 5 = highly confident. These are self-ratings, not test scores.")

    with st.expander("How I apply these skills"):
        st.write(
            "I apply backend and database concepts when developing application features, "
            "connecting services, managing data, and building APIs. I use frontend tools "
            "to create interfaces that allow users to interact with those features."
        )

elif page == "Projects":
    st.header("Selected Projects")
    st.write("A selection of academic software projects and the work I contributed.")
    tab1, tab2, tab3 = st.tabs(["ALLY", "DugoSugbo", "Loaner Request App"])

    with tab1:
        st.subheader("ALLY — AI-Powered Philippine Legal Assistant")
        st.markdown("**Role:** Primarily Backend Developer; also assisted with RAG integration and frontend tasks.")
        st.markdown("**Tools:** Spring Boot, Java, MySQL, ReactJS, Django, Python, Pinecone, and language-model APIs.")
        st.write(
            "A capstone project designed to help users explore Philippine legal information "
            "and relevant Supreme Court cases. It also includes a collaborative workspace "
            "concept for lawyer-client communication and document sharing."
        )
        st.info("Project focus: legal information retrieval and AI-assisted research. It is not intended to replace a lawyer.")
    with tab2:
        st.subheader("DugoSugbo — Blood Stock Management System")
        st.markdown("**Role:** Individual Developer")
        st.markdown("**Tools:** Kotlin, Spring Boot, ReactJS, MySQL")
        st.write(
            "An individual academic project designed to help monitor blood stock information "
            "and support coordination between blood banks, public hospitals, and local health facilities."
        )
        st.success("Key contribution: designed and developed the application across mobile, backend/web, and database components.")
    with tab3:
        st.subheader("Loaner Request App")
        st.markdown("**Role:** Student Developer")
        st.markdown("**Tools:** ServiceNow App Engine, Flow Designer, JavaScript")
        st.write(
            "A ServiceNow application developed while learning application development. "
            "It supports a loaner request workflow and provides practice with application "
            "configuration, roles, and platform automation."
        )
        st.info("Learning focus: ServiceNow application development and workflow configuration.")

    st.divider()
    st.subheader("Project reflection")
    st.write(
        "These projects helped me connect programming concepts with practical system "
        "requirements. They also taught me to consider data organization, user needs, "
        "integration between components, and the importance of testing."
    )

elif page == "Contact":
    st.header("Contact & Feedback")
    st.write("Have a question or feedback about my portfolio? You can leave a message below.")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email (optional)")
        reason = st.selectbox("What is your message about?", ["General feedback", "Project inquiry", "Collaboration", "Other"])
        rating = st.radio("How would you rate this portfolio?", ["Excellent", "Good", "Needs improvement"], horizontal=True)
        message = st.text_area("Your message", height=140)
        consent = st.checkbox("I confirm that this message is appropriate to share.")
        submitted = st.form_submit_button("Submit feedback", type="primary")

    if submitted:
        if not name.strip() or not message.strip():
            st.error("Please enter your name and a message before submitting.")
        elif not consent:
            st.warning("Please check the confirmation box before submitting.")
        else:
            st.session_state["last_feedback"] = {
                "name": name,
                "reason": reason,
                "rating": rating,
                "message": message,
            }
            st.success(f"Thank you, {name}! Your feedback has been recorded in this app session.")
            st.caption("Note: This demo form does not send email or permanently store submissions.")

    if "last_feedback" in st.session_state:
        with st.expander("View the latest submitted feedback"):
            st.write(st.session_state["last_feedback"])

    st.divider()
    st.subheader("Portfolio details")
    st.write("**Name:** John Lawrence Dioquino")
    st.write("**Program:** BS Information Technology, 4th Year")
    st.write("**University:** Cebu Institute of Technology–University")
    st.write("**Section:** G01")

# Footer
st.divider()
st.caption("© 2026 John Lawrence Dioquino · Autobiography and Portfolio ·")
