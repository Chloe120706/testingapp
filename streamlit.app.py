import streamlit as st

st.title(" My testing app:")
st.write("Let's start !")
usernames = ["123456"]
passwords = ["123456"] 
username = []
password = []

def sign(inorup):
    st.dialog("Sign %s:" % inorup)
    st.write("Username:")
    username.append(st.text_input("Write your username."))
    st.write("Password:")
    password.append(st.text_input("Write your password."))
    if st.button("Submit"):
        if username in usernames:
            if password == passwords(usernames.index(username)):
                st.write("Welcome %s !" % username)
            else:
                st.write("Your username or password is wrong, please try again! Or you can sign up.")
                st.button("Sign up")
                usernames.append(username)
                passwords.append(password)
        else:
            st.write("Your username or password is wrong, please try again! Or you can sign up.")

if st.button("Sign in"):
    sign("in")

if st.button("Sign up"):
    sign("up")