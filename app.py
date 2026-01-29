import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ntwanano Makhubele | Research Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------------- DARK MODE TOGGLE ----------------
dark_mode = st.sidebar.checkbox("Enable Dark Mode")

# ---------------- COLORS ----------------
if dark_mode:
    gradient_bg = "linear-gradient(135deg, #0F0F0F, #1A1A1A)"
    main_text = "#EAEAEA"
    header_color = "#4CAF50"
    card_bg = "#1F1F1F"
    card_shadow = "#00000066"
    link_color = "#4DA3FF"
else:
    gradient_bg = "linear-gradient(135deg, #F9F9F9, #E0E0E0)"
    main_text = "#111111"
    header_color = "#2E7D32"
    card_bg = "#FFFFFF"
    card_shadow = "#AAAAAA66"
    link_color = "#1A73E8"

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: {gradient_bg};
    color: {main_text};
}}

h1, h2, h3, h4, h5, h6 {{
    color: {header_color};
}}

a {{
    color: {link_color};
    text-decoration: none;
}}

hr {{
    border-color: #888;
}}

.card {{
    background-color: {card_bg};
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px {card_shadow};
    margin-bottom: 30px;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}}
.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 12px 40px {card_shadow};
}}

.skill-container {{
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    margin-bottom: 15px;
    overflow: hidden;
}}
.skill-fill {{
    background-color: #4CAF50;
    height: 28px;
    border-radius: 10px;
    text-align: right;
    color: #fff;
    font-weight: 600;
    width: 0%;
    padding-right: 10px;
    animation: fillBar 2s forwards;
}}
@keyframes fillBar {{
    from {{ width: 0%; }}
    to {{ width: var(--skill-width); }}
}}

.stButton>button {{
    background-color: {header_color};
    color: white;
    border-radius: 12px;
    padding: 8px 18px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}}
.stButton>button:hover {{
    background-color: #6fcf97;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

def go_back():
    st.session_state.page = "main"

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center'>👋 Hi, I'm Ntwanano Makhubele</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align:center; color:#555555'>BSc Mathematics & Physics | Research & Data Science Enthusiast</h3>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- MAIN PAGE ----------------
if st.session_state.page == "main":
    # --- RESEARCH INTERESTS ---
    st.markdown(f"""
    <div class="card">
    <h2>🔬 Research Interests</h2>
    <ul>
    <li>📊 Data Science & Statistical Modeling</li>
    <li>📐 Mathematical Modeling & Simulations</li>
    <li>🧪 Experimental Physics Analysis</li>
    <li>💻 Python for Research & Computational Projects</li>
    <li>📈 Data-driven Problem Solving</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Learn More about Research Interests", on_click=go_to, args=("interests",))

    # --- RESEARCH SKILLS ---
    st.markdown('<div class="card"><h2>🛠️ Research Skills</h2>', unsafe_allow_html=True)
    skills = {
        "Python for Data Analysis": "90%",
        "Statistical Modeling & Simulation": "85%",
        "Mathematical Modeling": "80%",
        "Machine Learning (Research Projects)": "75%",
        "Data Visualization (Matplotlib, Seaborn)": "80%",
        "Git & GitHub": "80%"
    }
    for skill, width in skills.items():
        st.markdown(f"""
        <div class="skill-container">
            <div class="skill-fill" style="--skill-width:{width}">{skill}</div>
        </div>
        """, unsafe_allow_html=True)
    st.button("Learn More about Skills", on_click=go_to, args=("skills",))
    st.markdown('</div>', unsafe_allow_html=True)

    # --- RESEARCH PROJECTS / PUBLICATIONS ---
    st.markdown(f"""
    <div class="card">
    <h2>📚 Research Projects / Publications</h2>
    <ul>
    <li>📌 Data Science Internship Tasks – Prodigy Infotech</li>
    <li>📌 Exploratory Data Analysis of Experimental Physics Data</li>
    <li>📌 Python-based simulations and modeling projects</li>
    <li>📌 Statistical analysis of research datasets</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Learn More about Projects", on_click=go_to, args=("projects",))

    # --- EDUCATION ---
    st.markdown(f"""
    <div class="card">
    <h2>🎓 Education</h2>
    <ul>
    <li>🏫 University of Venda – BSc Mathematics & Physics</li>
    <li>📚 Relevant Courses: Data Science, Statistics, Machine Learning, Mathematical Modeling</li>
    <li>🎓 Research Internships: Prodigy Infotech</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Learn More about Education", on_click=go_to, args=("education",))

# ---------------- DETAILED PAGES ----------------
elif st.session_state.page == "interests":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>🔬 Detailed Research Interests</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Advanced statistical modeling of experimental datasets</li>
        <li>Simulation of physical systems using Python and MATLAB</li>
        <li>Computational approaches to data-driven research</li>
        <li>Machine learning applied to experimental physics</li>
    </ul>
    """, unsafe_allow_html=True)
    st.button("Back", on_click=go_back)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>🛠️ Detailed Research Skills</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Python: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn</li>
        <li>Data Analysis & Statistical Modeling</li>
        <li>Mathematical & Physical Simulations</li>
        <li>Machine Learning for research</li>
        <li>Git & GitHub for project management</li>
    </ul>
    """, unsafe_allow_html=True)
    st.button("Back", on_click=go_back)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>📚 Detailed Research Projects / Publications</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Data Science Internship Tasks at Prodigy Infotech: data cleaning & EDA</li>
        <li>Exploratory Data Analysis of Physics Experiment Data</li>
        <li>Python-based simulation of mathematical models</li>
        <li>Statistical analysis and visualization for research papers</li>
    </ul>
    """, unsafe_allow_html=True)
    st.button("Back", on_click=go_back)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "education":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>🎓 Detailed Education</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>University of Venda – BSc Mathematics & Physics</li>
        <li>Relevant Courses: Data Science, Statistics, Machine Learning, Mathematical Modeling</li>
        <li>Research Internships: Prodigy Infotech</li>
        <li>Workshops & Seminars attended for advanced research skills</li>
    </ul>
    """, unsafe_allow_html=True)
    st.button("Back", on_click=go_back)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.markdown(f"""
<div class="card">
<h2>📬 Contact</h2>
<p>
🔗 LinkedIn:
<a href="https://www.linkedin.com/in/ntwanano-makhubele" target="_blank">
linkedin.com/in/ntwanano-makhubele
</a><br><br>
🧑‍💻 GitHub:
<a href="https://github.com/NtwananoMakhubele" target="_blank">
github.com/NtwananoMakhubele
</a>
</p>
</div>
""", unsafe_allow_html=True)

st.success("Thank you for visiting my research portfolio 🚀")
