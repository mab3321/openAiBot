import openai
from dotenv import dotenv_values

# Load configuration from .env file
config = dotenv_values(".env")


class ChatGptBotAPI:
    def __init__(self, openaikey):
        # Initialize the OpenAI API with the provided API key
        openai_api_key = config.get("OPENAI_API_KEY")
        openai.api_key = openai_api_key
        self.prompts = []

    def get_response(self, prompt):
        try:
            # Generate a response from the OpenAI GPT model using the provided prompt
            response_from_api = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
            )
            response_to_send = response_from_api.choices[0]['message']['content']
            return response_to_send
        except Exception as e:
            return "Encountered Error."

    def create_prompt(self, prompt):
        # Add a new prompt to the list of prompts
        self.prompts.append(prompt)

    def read_prompt(self, index=None):
        if index is None:
            # Return the list of all prompts
            return self.prompts
        if 0 <= index < len(self.prompts):
            # Return the prompt at the specified index
            return self.prompts[index]
        else:
            # Return None for invalid index
            return None

    def update_prompt(self, index, new_message):
        if 0 <= index < len(self.prompts):
            # Update the prompt at the specified index with a new message
            self.prompts[index] = new_message
        else:
            # Raise an IndexError for index out of range
            raise IndexError("Index out of range")

    def delete_prompt(self, index):
        if 0 <= index < len(self.prompts):
            # Delete the prompt at the specified index
            del self.prompts[index]
        else:
            # Raise an IndexError for index out of range
            raise IndexError("Index out of range")
