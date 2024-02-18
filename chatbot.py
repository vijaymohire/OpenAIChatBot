import requests

api_key = ''

def chat_with_bot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        response = get_openai_response(user_input)
        print("Chatbot:", response)

def get_openai_response(user_input):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful chatbot.'},
                     {'role': 'user', 'content': user_input}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

if __name__ == "__main__":
    chat_with_bot()
