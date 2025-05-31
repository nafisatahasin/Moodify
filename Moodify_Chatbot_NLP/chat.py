import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load model
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

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

# Mood-based extras
mood_resources = {
    "sadness": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "journal": "Write about a moment that made you feel supported."
    },
    "anxiety": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
        "journal": "List 3 things you can control right now."
    },
    "burnout": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7",
        "journal": "Describe a recent moment of joy, even if small."
    },
    "happiness": {
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "journal": "What made you smile today?"
    }
}

bot_name = "MoodMate"
print(f"{bot_name}: Hi, I’m {bot_name}. How are you feeling today? (type 'quit' to stop)")

while True:
    sentence = input("You: ")
    if sentence.lower() == "quit":
        break

    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = torch.from_numpy(X).float().unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.7:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent["responses"])
                print(f"{bot_name}: {response}")

                if tag in mood_resources:
                    print(f"🎧 Here's a playlist to match your mood: {mood_resources[tag]['spotify']}")
                    print(f"📝 Journal prompt: {mood_resources[tag]['journal']}")
                break
    else:
        print(f"{bot_name}: I'm not sure I understand. Could you rephrase?")
    
