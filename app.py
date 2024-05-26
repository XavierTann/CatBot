import os
import json
import openai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Flask app
app = Flask(__name__)

# Function to call CatAPI
def get_cat_images(limit, breed):
    url = 'https://api.thecatapi.com/v1/images/search'
    params = {'limit': limit, 'breed_id': breed}
    headers = {
        'x-api-key': os.getenv("CAT_API_KEY")  # Add your Cat API key here
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []

function_descriptions = [
    {
        "name": "get_cat_images",
        "description": "Get cat images by the breed",
        "parameters": {
            "type": "object",
            "properties": {
                "breed": {
                    "type": "string",
                    "description": "The breed of the cat, indexed by the first 4 letters, e.g. abys",
                },
                "limit": {
                    "type": "integer",
                    "description": "The number of cat images, e.g. 3",
                },
            },

        },
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": user_input}],
        functions=function_descriptions,
        function_call="auto",
    )

    output = completion.choices[0].message

    response = "Please key in cat breed."
    image_urls = None

    if output.get("function_call"):
        params = json.loads(output["function_call"]["arguments"])
        limit = params.get("limit")
        breed = params.get("breed")

        cat_images = get_cat_images(limit, breed)
        image_urls = [img['url'] for img in cat_images]
        function_response = json.dumps(cat_images)

        second_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "I do not want any URLs or links in the response. I just want one fun fact about the cat breed in the first line."},
                {"role": "user", "content": user_input},
                {"role": "function", "name": output["function_call"]["name"], "content": function_response},
            ],
            functions=function_descriptions,
        )
        response = second_completion.choices[0].message.content
    

    return jsonify({"message": response, "cat_images": image_urls})

if __name__ == '__main__':
    app.run(debug=True)
