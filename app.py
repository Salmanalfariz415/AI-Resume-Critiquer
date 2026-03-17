import streamlit as st
import home
import resume

# ✅ MUST initialize BEFORE using
if "page" not in st.session_state:
    st.session_state.page = "home"

st.set_page_config(layout="wide")

# Remove sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# Conditional navigation
if st.session_state.page == "home":
    if st.button("📄 Resume Critiquer"):
        st.session_state.page = "resume"
        st.rerun()
else:
    if st.button("← Go Back"):
        st.session_state.page = "home"
        st.rerun()

st.divider()

# Routing
if st.session_state.page == "home":
    home.show()
else:
    resume.show()