import streamlit as st
import requests

st.title("Logo creation agent")

description = st.text_input("Enter your description")
# cols = st.columns([.25, .25, .25, .25])
if st.button("Create Logo"):
    st.subheader("Logo creation result")
    with st.spinner("generating logo"):
        results = requests.get("http://127.0.0.1:8000/create_logo/", params={"description": description}).json()

    cols = st.columns([.25, .25, .25, .25])
    for i, image in enumerate(results):
        url = image['url']
        with cols[i]:
            st.image(url)