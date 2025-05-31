💙 Moodify - Your AI-Powered Mental Health Companion
Moodify is an AI-driven mental health chatbot that helps users check in on their emotional well-being, journal their thoughts, and access personalized self-care resources like Spotify music suggestions and breathing exercises.

🧠 Key Features
Conversational AI: Engages users with empathetic responses based on emotion recognition.

Mood Journaling: Allows users to log their feelings and thoughts privately.

Spotify Music Integration: Recommends mood-based music to uplift or calm users.

Breathing Exercises: Offers guided calming techniques to help users manage anxiety.

Intelligent Suggestions: Responds with relevant coping strategies using NLP.

🏗️ Project Structure
![image](https://github.com/user-attachments/assets/8a285c38-8982-4404-ba3e-720530484485)
🧰 Tech Stack
🔙 Backend
Python

Flask – Web framework to handle routes, API requests, and render HTML.

PyTorch – For building and training the neural network model that performs intent classification.

NLTK – Tokenization, stemming, and natural language preprocessing.

🤖 Machine Learning
Feedforward Neural Network – Trained on custom intents to predict user intent.

Preprocessing – Text inputs are tokenized, stemmed, and converted to bag-of-words vectors.

Model Training – train.py uses PyTorch to train on intents.json.

🌐 Frontend
HTML/CSS – User interface for chatting, journaling, and breathing.

JavaScript (optional) – For dynamic interactions, if added.

🎵 Integrations
Spotify API (Planned/Optional) – For fetching mood-based playlists or songs.

Local Journal Logging – Saves user entries for reflection.

🚀 How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/Moodify.git
   cd Moodify
Create a virtual environment & activate:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install flask torch nltk

Download NLTK resources:

import nltk
nltk.download('punkt')

Train the model (only once):

python train.py

Run the app:

python app1.py

Open in browser:

http://127.0.0.1:5000/

✨ Future Enhancements

✅ PDF export of journal logs

✅ Spotify mood-based playlist integration

✅ Emotion classification using deep learning

⏳ Dark mode UI

⏳ Progress tracking dashboard

🤝 Contributing
Feel free to fork, enhance, and raise issues. Mental health matters — let’s make tech accessible and supportive.


