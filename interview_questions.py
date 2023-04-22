import random
import requests
import openai

# initialize OpenAI GPT-3 API key
openai.api_key = "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"

def retrieve_keywords(topic):
    # Assuming the API returns JSON data with a 'keywords' field.
    # Replace with the actual API URL and parameters if necessary.
    url = f"https://api.getkeywords.io/keywords?topic={topic}"
    response = None
    attempts = 0
    while response is None:
        try:
            response = requests.get(url)
            keywords = response.json()["keywords"]
            return random.sample(keywords, 3)
        except requests.exceptions.RequestException as e:
            attempts += 1
            if attempts > 3:
                print("Error: Maximum number of retry attempts exceeded. Exiting.")
                exit()
            print("Error: " + str(e))
            print("Retrying in 5 seconds...")
            time.sleep(5)

def generate_interview_questions(topic):
    # Retrieving 3 keywords from API.
    keywords = retrieve_keywords(topic)
    questions = []
    for keyword in keywords:
        prompt = f"Generate an interview question related to {keyword}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt + "\nAI:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        question = response.choices[0].text.strip()
        questions.append(question)
    return questions
