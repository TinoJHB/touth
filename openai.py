
import openai


# initialize OpenAI GPT-3 API key
openai.api_key = "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"

# define function to process user input using OpenAI chatbot
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
