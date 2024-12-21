import nltk
from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.corpus import wordnet

# Add local nltk_data to path
nltk.data.path.append("./nltk_data")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_meaning():
    word = request.args.get("word", "").strip()
    if not word:
        return jsonify({"error": "Please provide a word to look up."}), 400

    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        return jsonify({"word": word, "meaning": definition})
    else:
        return jsonify({"word": word, "meaning": "No definition found."}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
