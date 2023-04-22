import speech_recognition as sr
import pyttsx3
import time
import random
import streamlit as st
from interview_topic import get_interview_topic
from interview_questions import generate_interview_questions
from interview_data import save_interview_data
from speech import speak
from ui import run_ui

# initialize the speech recognizer
r = sr.Recognizer()

# initialize text-to-speech engine
engine = pyttsx3.init()

# define function to process user input
def process_input(input_text=None):
    if input_text is None:
        # set default prompt here
        input_text = "Hello, how can I assist you today?"

    # send the input text to the OpenAI chatbot
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text + "\nAI:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # return the chatbot's response text
    return response.choices[0].text.strip()

def main():
    interview_topic = get_interview_topic()
    interview_questions = generate_interview_questions(interview_topic)
    print(interview_questions)

    # prompt user to answer interview questions
    speak(f"Please answer the following questions about {interview_topic}.")
    interview_data = []
    for question in interview_questions:
        speak(question)
        with sr.Microphone() as source:
            print("Please say your answer...")
            audio = r.listen(source)

        try:
            # convert audio to text using Google Speech Recognition API
            input_text = r.recognize_google(audio)
            print("You said: " + input_text)

            # assess the user's answer using the OpenAI chatbot
            response_text = process_input(f"How well did I answer the question: {input_text}?\nAI:")
            speak(response_text)

            # store the question and answer
            interview_data.append({"question": question, "answer": input_text, "assessment": response_text})

        except Exception as e:
            print("Error: " + str(e))

    # Save interview data to a file
    save_interview_data(interview_data)

if __name__ == "__main__":
    # ask for permission to access the microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Hello I'm Thoth-AI. I'm the god of wisdom. May you please grant permission to access your microphone so we can start training.")
        time.sleep(1)
    run_ui(main)
