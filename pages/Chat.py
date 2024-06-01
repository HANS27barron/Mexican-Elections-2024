import streamlit as st
from openai import OpenAI

OPENAI_API = st.secrets["OPENAI_API_KEY"]


st.title("Bot random")


client = OpenAI(api_key=OPENAI_API)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Escribe algo")
if prompt:
     #with st.chat_message("user"):
      #   st.markdown(f"You: {prompt}")

    st.chat_message("user").markdown(f"You:{prompt}")
    st.session_state.messages.append({"role": "user", "content":prompt})
    response = f"RandomBot:{prompt}"

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content":prompt})