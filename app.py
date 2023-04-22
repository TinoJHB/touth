import streamlit as st
from main import main

def run_main():
    main()

st.title("Thoth-AI Interview Bot")

if st.button("Start Interview"):
    run_main()
