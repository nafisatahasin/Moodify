from flask import Flask, render_template, request, jsonify
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load intents
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Load model
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# Spotify setup using credentials from .env
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Mood-based Spotify playlists and journal prompts
mood_resources = {
    "sadness": {
        "spotify": "https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "journal": "Write about a moment that made you feel supported, even if it was small."
    },
    "anxiety": {
        "spotify": "https://open.spotify.com/embed/playlist/37i9dQZF1DX3rxVfibe1L0",
        "journal": "What’s one thing you can control right now? Write it down."
    },
    "burnout": {
        "spotify": "https://open.spotify.com/embed/playlist/37i9dQZF1DX6VdMW310YC7",
        "journal": "Describe a time when you felt fulfilled. What were you doing?"
    },
    "happiness": {
        "spotify": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
        "journal": "What’s something today that made you smile?"
    }
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    sentence = request.form["msg"]
    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = torch.from_numpy(X).float().unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    response_data = {"response": "", "spotify": None, "journal": None}

    if prob.item() > 0.7:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response_data["response"] = random.choice(intent["responses"])
                if tag in mood_resources:
                    response_data["spotify"] = mood_resources[tag]["spotify"]
                    response_data["journal"] = mood_resources[tag]["journal"]
                break
    else:
        response_data["response"] = "I'm not sure I understand. Could you rephrase?"

    return jsonify(response_data)
