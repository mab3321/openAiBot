import openai
import os
from dotenv import dotenv_values
config = dotenv_values(".env")


class ChatGptBotAPI:
    def __init__(self, openaikey):

        openai_api_key = config.get("OPENAI_API_KEY")
        openai.api_key = openai_api_key
        self.prompts = []

    def get_response(self, prompt):

        try:
            response_from_api = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
            response_to_send = response_from_api.choices[0]['message']['content']
            return response_to_send
        except Exception as e:
            return "Encountered Error."

    def create_prompt(self, prompt):
        self.prompts.append(prompt)

    def read_prompt(self, index=None):
        if index is None:
            return self.prompts
        if 0 <= index < len(self.prompts):
            return self.prompts[index]
        else:
            return None

    def update_prompt(self, index, new_message):
        if 0 <= index < len(self.prompts):
            self.prompts[index] = new_message
        else:
            raise IndexError("Index out of range")

    def delete_prompt(self, index):
        if 0 <= index < len(self.prompts):
            del self.prompts[index]
        else:
            raise IndexError("Index out of range")


# Usage
openai_api_key = config.get("OPENAI_API_KEY")
print(openai_api_key)
bot = ChatGptBotAPI(openai_api_key)

# Create messages
bot.create_prompt("Hello there!")
bot.create_prompt("How can I help you?")
bot.create_prompt("Feel free to ask any questions.")

# Read messages
print("All messages:", bot.read_prompt())
print("Message at index 1:", bot.read_prompt(1))

# Update message
bot.update_prompt(0, "Greetings!")
print("Updated messages:", bot.read_prompt())

# Delete message
bot.delete_prompt(2)
print("Remaining messages:", bot.read_prompt())
