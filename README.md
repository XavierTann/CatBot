# CatBot

CatBot is a chatbot application that allows users to interact with an AI-powered chatbot to get fun facts about different cat breeds and view images of cats. The chatbot is built using Flask, OpenAI's GPT-3.5-turbo, and TheCatAPI.

## Features

- Chat with an AI-powered bot to learn fun facts about different cat breeds.
- Retrieve and display cat images based on the breed specified.
- User-friendly web interface for easy interaction.

## Technologies Used

- Flask
- OpenAI GPT-3.5-turbo
- TheCatAPI
- HTML/CSS/JavaScript

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- OpenAI API key
- TheCatAPI key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/catbot.git
cd catbot
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory and add your OpenAI API key and TheCatAPI key:

```
OPENAI_API_KEY=your_openai_api_key
CAT_API_KEY=your_cat_api_key
```

### Running the Application

1. Start the Flask app:

```bash
flask run
```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to start chatting with CatBot.

## Usage

1. Enter your message in the input field and press "Send".
2. CatBot will respond with a fun fact about the specified cat breed and display images of cats if applicable.
3. Enjoy chatting and viewing cat images!

## File Structure

```
catbot/
├── templates/
│   └── index.html         # HTML template for the web interface
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables (not included in version control)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for the GPT-3.5-turbo model.
- [TheCatAPI](https://thecatapi.com/) for providing cat images.
- Flask framework for building the web application.

## Contact

For any questions or suggestions, please contact xavier.internships@gmail.com

Enjoy chatting with CatBot and discovering fun facts about your favorite cat breeds! 🐱

