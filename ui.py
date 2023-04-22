import streamlit as st
import time

def run_ui(main_func):
    st.set_page_config(page_title="Thoth-AI", page_icon=":books:")

    st.title("Thoth-AI")

    st.write("Welcome to Thoth-AI, the god of wisdom. Please click the button below to start training.")

    if st.button("Train Thoth-AI"):
        st.write("Training started...")
        main_func()
        st.write("Training complete!")
