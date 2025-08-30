import streamlit as st
st.title("Welcome!")

@st.dialog("Sign out")
def sign():
    st.write("Are you sure sign out?")
    if st.button("Sure"):
        st.page_link("streamlit.app.py", label="Sign out", icon="")

if "sign" not in st.session_state:
    if st.button("Sign out"):
        sign()

