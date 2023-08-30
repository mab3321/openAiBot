from index import ChatGptBotAPI
from flask import Flask, request, jsonify
from dotenv import dotenv_values
config = dotenv_values(".env")
app = Flask(__name__)

openai_api_key = config.get("OPENAI_API_KEY")
bot = ChatGptBotAPI(openai_api_key)


@app.route('/create', methods=['POST'])
def create_prompt():
    data = request.json
    prompt = data.get('prompt')
    bot.create_prompt(prompt)
    return jsonify({"message": "Prompt created successfully"}), 201


@app.route('/read', methods=['GET'])
def read_prompt():
    index = int(request.args.get('index', None))
    prompts = bot.read_prompt(index)
    if prompts is None:
        return jsonify({"error": "Invalid index"}), 400
    return jsonify({"prompts": prompts}), 200


@app.route('/get_response', methods=['GET'])
def get_response():
    index = int(request.args.get('index', None))
    print(index)
    prompts = bot.read_prompt(index)
    if prompts is None:
        return jsonify({"error": "Invalid index"}), 400
    response = bot.get_response(prompts)
    return jsonify({"response": response}), 200


@app.route('/update', methods=['PUT'])
def update_prompt():
    data = request.json
    index = data.get('index')
    new_prompt = data.get('new_prompt')
    try:
        bot.update_prompt(index, new_prompt)
        return jsonify({"message": "Prompt updated successfully"}), 200
    except IndexError:
        return jsonify({"error": "Invalid index"}), 400


@app.route('/delete', methods=['DELETE'])
def delete_prompt():
    data = request.json
    index = data.get('index')
    try:
        bot.delete_prompt(index)
        return jsonify({"message": "Prompt deleted successfully"}), 200
    except IndexError:
        return jsonify({"error": "Invalid index"}), 400


if __name__ == '__main__':
    app.run(debug=True)
