import streamlit as st

st.title(" My testing app:")
st.write("Let's start !")
usernames = ["123456"]
passwords = ["123456"] 

@st.dialog("Cast your vote")
def sign(item):
    st.write(f"Sign{item}")
    username = st.text_input("Username:")
    password = st.text_input("Password:")
    psindex = passwords.index(password)
    if st.button("Submit"):
        if username in usernames:
            if password == psindex:
                st.session_state.sign = {"username": username}
                st.rerun()
            else:
                st.wirte("Your username or password is wrong, please try again, or you can sign up.")
    else:
        if item == "up":
            usernames.append(username)
            passwords.append(password)
            st.write("Please sign in again!")
    st.write("Your username or password is wrong, please try again, or you can sign up.")
       

if "sign" not in st.session_state:
    if st.button("Sign in"):
        sign("in")
    if st.button("Sign up"):
        sign("up")
else:
    st.write(f"Welcome {st.session_state.sign['item']}!")
    

