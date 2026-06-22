# OpenAI API Exploration
**Project URL:**https://roadmap.sh/projects/openai-api-python
**Project Page:** [https://github.com/AnmolS05/OpenAI-API-in-Python](https://github.com/AnmolS05/OpenAI-API-in-Python)

This project demonstrates how to set up and use the OpenAI Python API, including configuring the client, managing environment variables, exploring parameters, and building a simple interactive chatbot.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables:**
   - Copy `.env.example` to a new file named `.env`.
   - Add your OpenAI API key to the `.env` file.

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Instructions to Run the Project

1. **`01_basic_call.py`**: Demonstrates initializing the client and making a single API call while experimenting with `temperature`, `max_tokens`, and `system message` parameters.
   ```bash
   python 01_basic_call.py
   ```
2. **`02_interactive_script.py`**: A small console-based chatbot that takes continuous user input and returns responses from the model.
   ```bash
   python 02_interactive_script.py
   ```
3. **`03_temperature_comparison.py`**: Sends the same prompt to the model multiple times using different temperature values to compare the deterministic versus creative nature of the outputs.
   ```bash
   python 03_temperature_comparison.py
   ```
