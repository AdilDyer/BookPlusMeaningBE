import os
import nltk
from nltk.corpus import wordnet
from flask import Flask, request, jsonify
from flask_cors import CORS

# Set the NLTK data path to the folder where nltk_data is located
os.environ['NLTK_DATA'] = './nltk_data'

# Check if wordnet data is available, otherwise, download it
# This step ensures that it won't try to download again if the data is already present
if not os.path.exists('./nltk_data/corpora/wordnet.zip'):
    nltk.download('wordnet')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Endpoint to return word meaning
@app.route('/', methods=['GET'])
def get_meaning():
    # Fetch 'word' query parameter
    word = request.args.get('word', '').strip()
    if not word:
        return jsonify({"error": "Please provide a word to look up."}), 400

    # Find the meaning of the word
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        return jsonify({"word": word, "meaning": definition})
    else:
        return jsonify({"word": word, "meaning": "No definition found."}), 404
