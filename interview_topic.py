import pyttsx3
import time
import logging
import speech_recognition as sr

# initialize the speech recognizer
r = sr.Recognizer()

# initialize text-to-speech engine
engine = pyttsx3.init()

# set up logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def speak(text):
    """
    Convert text to speech and play it through the system's default audio device.
    """
    engine.say(text)
    engine.runAndWait()

def get_interview_topic():
    """
    Use speech recognition to get the user's desired interview topic.
    """
    attempts = 0
    source = None
    with sr.Microphone() as source:
        speak("Please tell me the topic you would like to be interviewed on.")
        logging.info('Prompting user for interview topic...')
        print("Listening for the topic...")

        # listen for user input with a timeout of 15 seconds
        audio = r.listen(source, timeout=15)

        try:
            # convert audio to text using Google Speech Recognition API
            logging.info('Transcribing user input...')
            interview_topic = r.recognize_google(audio)
            logging.info(f'User input: {interview_topic}')
            print("You said: " + interview_topic)
            return interview_topic

        except Exception as e:
            logging.error(f'Error transcribing user input: {str(e)}')
            attempts += 1
            speak("I couldn't understand the topic. Please try again.")

            # prompt the user again up to 2 more times if they don't respond
            if attempts < 2:
                return get_interview_topic()
            else:
                logging.warning('Maximum number of attempts exceeded.')
                speak("Sorry, I couldn't understand the topic. Shutting down.")
                exit()

if __name__ == '__main__':
    get_interview_topic()
    logging.info('Getting interview topic...')
    # Add additional network-related activity here
