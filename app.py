# Import necessary modules
from chat_gpt_bot_api import ChatGptBotAPI
from flask import Flask, request, jsonify
from dotenv import dotenv_values

# Load configuration from .env file
config = dotenv_values(".env")

# Initialize Flask app
app = Flask(__name__)

# Get the OpenAI API key from the config
openai_api_key = config.get("OPENAI_API_KEY")

# Initialize the ChatGptBotAPI instance with the OpenAI API key
bot = ChatGptBotAPI(openai_api_key)

# Endpoint to create a new prompt


@app.route('/create', methods=['POST'])
def create_prompt():
    data = request.json
    prompt = data.get('prompt')
    bot.create_prompt(prompt)
    return jsonify({"message": "Prompt created successfully"}), 201

# Endpoint to read a prompt


@app.route('/read', methods=['GET'])
def read_prompt():
    index = int(request.args.get('index', None))
    prompts = bot.read_prompt(index)
    if prompts is None:
        return jsonify({"error": "Invalid index"}), 400
    return jsonify({"prompts": prompts}), 200

# Endpoint to get a response based on a prompt


@app.route('/get_response', methods=['GET'])
def get_response():
    index = int(request.args.get('index', None))
    prompts = bot.read_prompt(index)
    if prompts is None:
        return jsonify({"error": "Invalid index"}), 400
    response = bot.get_response(prompts)
    if response != "Encountered Error.":
        return jsonify({"response": response}), 200
    else:
        return jsonify({"Error": response}), 400
# Endpoint to update a prompt


@app.route('/update', methods=['PUT'])
def update_prompt():
    data = request.json
    index = data.get('index')
    new_prompt = data.get('new_prompt')
    try:
        bot.update_prompt(index, new_prompt)
        return jsonify({"message": "Prompt updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Invalid index"}), 400

# Endpoint to delete a prompt


@app.route('/delete', methods=['DELETE'])
def delete_prompt():
    data = request.json
    index = data.get('index')
    try:
        bot.delete_prompt(index)
        return jsonify({"message": "Prompt deleted successfully"}), 200
    except IndexError:
        return jsonify({"error": "Invalid index"}), 400


# Run the app if this is the main script
if __name__ == '__main__':
    port = config.get('port')
    print(port)
    app.run(host="0.0.0.0", port=port)
