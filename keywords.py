import random
import requests

def retrieve_keywords(topic):
    # Replace 'YOUR_API_KEY' with your actual TextRazor API key.
    api_key = 'e4f4314a31fb5fc13277d38368c1014ba55b2c85d32e6b0bbd970089'
    
    # Set up the request parameters.
    headers = {'X-TextRazor-Key': api_key}
    params = {'extractors': 'entities,topics', 'entity_type': 'Noun', 'limit': 3}
    
    # Replace 'YOUR_TEXT' with your actual topic.
    data = {'text': topic}
    
    # Send the request to the TextRazor API.
    response = requests.post('https://api.textrazor.com/', headers=headers, params=params, data=data)
    response.raise_for_status()
    
    # Parse the response to extract the keywords.
    keywords = []
    for entity in response.json()['response']['entities']:
        keywords.append(entity['matchedText'])
    for topic in response.json()['response']['topics']:
        keywords.append(topic['label'])
    return random.sample(keywords, 3)

