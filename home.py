import streamlit as st

# pip install streamlit
# streamlit run home.py
# https://docs.streamlit.io/develop/concepts/architecture/run-your-app

st.title("this is another page")

if st.button("this is a button"):
    st.write("you clicked the button")
    st.warning("this is a warning")