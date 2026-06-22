import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    """
    Initialize the OpenAI client and make a basic API call.
    Demonstrates the use of system messages, temperature, and max_tokens.
    """
    load_dotenv()
    
    # The client automatically looks for the OPENAI_API_KEY environment variable
    client = OpenAI()
    
    print("Making a basic API call to OpenAI...\n")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and concise assistant."},
                {"role": "user", "content": "Explain the concept of an API in one sentence."}
            ],
            temperature=0.7,
            max_tokens=50
        )
        
        print("Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
