import os
from dotenv import load_dotenv
from openai import OpenAI

def run_chatbot():
    """
    Run a simple interactive chatbot using the OpenAI API.
    Takes user input continuously until the user types 'exit' or 'quit'.
    """
    load_dotenv()
    client = OpenAI()
    
    print("=== Interactive OpenAI Chatbot ===")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    # Store conversation history to maintain context
    conversation_history = [
        {"role": "system", "content": "You are a helpful conversational assistant."}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                temperature=0.7,
                max_tokens=150
            )
            
            assistant_message = response.choices[0].message.content
            print(f"Assistant: {assistant_message}\n")
            
            conversation_history.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    run_chatbot()
