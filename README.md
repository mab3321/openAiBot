# ChatGptBotAPI Flask Application

This is a Flask application that provides an API for interacting with the ChatGptBotAPI, allowing you to create, read, update, and delete prompts, and get responses from the OpenAI GPT-3 model.

## Features

- Create a new prompt
- Read prompts by index or get responses from prompts
- Update prompts
- Delete prompts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-chatgptbotapi-flask-app.git
   cd your-chatgptbotapi-flask-app```
2. Install dependencies using pip:
     ```bash
     pip install -r requirements.txt```
Set up your .env File:
    Rename the .env.example file to **.env** and replace **OPENAI_API_KEY** with your actual OpenAI API key.
Run the Flask application:
  ```bash
  python app.py```
Access the endpoints using HTTP requests. You can use tools like curl or software like Postman for testing.
For Getting The Collections You can Use Following Link :
https://grey-robot-983360.postman.co/workspace/New-Team-Workspace~5ccf99c2-888d-498b-8b6d-afcc04e9ec57/collection/24157295-0dae2534-ded7-4e59-aa82-f5d6a502d92b?action=share&creator=24157295
## Endpoints
POST /create: Create a new prompt.
GET /read?index=<index>: Read a prompt by index.
GET /get_response?index=<index>: Get a response from a prompt.
PUT /update: Update a prompt.
DELETE /delete: Delete a prompt
## Testing
To run the unit tests, you can use the following command:
    ```bash
        python test.py```
## Using Docker
You can also run the application using Docker for easy containerization:

  ## Build the Docker image:
      ```bash
            docker build -t chatgptbotapi-flask-app .```
  ## Run the Docker container:
      ```bash
            docker run -p 5000:5000 chatgptbotapi-flask-app```
  Access the endpoints as usual.






.
