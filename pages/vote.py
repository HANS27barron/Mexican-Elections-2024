import streamlit as st

@st.experimental_dialog("Account")
def vote(item):
    st.write(item)
    reason = st.text_input("Enter your mail")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Log in to your account or create a new one!")
    if st.button("Log in"):
        vote("Log in")
    if st.button("Create new account"):
        vote("Create new account")
else:
    st.write("{st.session_state.vote['item']}: {st.session_state.vote['reason']}")