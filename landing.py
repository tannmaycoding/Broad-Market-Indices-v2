import streamlit as st

st.title("Broad Market Indices Historical Prices")
st.text("Get The Broad Market Indices Prices and Download Them, See the graph of them")

if st.button("Log In"):
    st.switch_page("pages/page_1.py")

if st.button("Sign Up"):
    st.switch_page("pages/page_2.py")

if st.button("Try as a Guest"):
    st.switch_page("pages/page_4.py")
