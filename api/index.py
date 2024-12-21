import nltk
from nltk.corpus import wordnet
from flask import Flask, request, jsonify
from flask_cors import CORS

# Download the WordNet corpus (only needed once)
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

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5000)
# Entry point for Vercel
def handler(event, context):
    from flask import request
    return app(event, context)
