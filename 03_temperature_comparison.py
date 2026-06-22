import os
from dotenv import load_dotenv
from openai import OpenAI

def compare_temperatures(prompt: str, temperatures: list[float]):
    """
    Compare OpenAI model outputs for the same prompt across different temperature values.
    
    Args:
        prompt: The user prompt to send to the model.
        temperatures: A list of float temperature values to test.
    """
    load_dotenv()
    client = OpenAI()
    
    print(f"Prompt: '{prompt}'\n")
    print("-" * 50)
    
    for temp in temperatures:
        print(f"Temperature: {temp}")
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temp,
                max_tokens=100
            )
            print(f"Response:\n{response.choices[0].message.content}\n")
        except Exception as e:
            print(f"An error occurred at temperature {temp}: {e}\n")
        print("-" * 50)

def main():
    """
    Execute the temperature comparison with predefined values.
    """
    test_prompt = "Write a short, two-line poem about a robot learning to feel."
    test_temperatures = [0.0, 0.7, 1.5]
    
    compare_temperatures(test_prompt, test_temperatures)

if __name__ == "__main__":
    main()
