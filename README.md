Cat Chatbot

A simple Flask-based chatbot that provides cat images and fun facts about cat breeds using OpenAI's GPT-3.5-turbo-0613 model and The Cat API.

Features

Chat Interface: Allows users to interact with the bot.
Retrieve Cat Images: Fetches cat images based on the breed specified by the user.
Fun Facts: Provides interesting facts about the specified cat breed along with images.
How It Works

User Interaction: Users interact with the chatbot through a web interface.
Breed Request: Users can request images of specific cat breeds by typing messages like "Show me images of Siamese cats."
API Integration:
The bot uses OpenAI's GPT-3.5-turbo-0613 model to process user inputs and determine the required action.
The bot fetches cat images from The Cat API based on the breed provided by the user.
Response: The bot responds with a fun fact about the requested cat breed and displays the images.
Project Structure

bash
Copy code
cat-chatbot/
├── templates/
│   └── index.html  # HTML template for the chat interface
├── app.py          # Main Flask application
├── .env            # Environment variables file (add your API keys here)
├── requirements.txt # Python dependencies
└── README.md       # This readme file
Packages Used

Flask: A micro web framework for Python.
Requests: A simple HTTP library for Python, used to interact with The Cat API.
OpenAI: The official OpenAI API client for accessing GPT-3.5-turbo-0613.
