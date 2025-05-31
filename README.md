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
Clone the repo:
![image](https://github.com/user-attachments/assets/16c8a023-9efe-424d-8a74-f89c3edee2db)
Create a virtual environment & activate:
![image](https://github.com/user-attachments/assets/8f30d723-5344-4048-82fa-411e520b5f12)
Install dependencies:
![image](https://github.com/user-attachments/assets/0c87cc52-24ea-4957-b480-2f6f00703fb7)
Download NLTK resources:
![image](https://github.com/user-attachments/assets/73cd99a9-620a-4fcf-98c4-e0b5b565bb61)
Train the model (only once):
![image](https://github.com/user-attachments/assets/d5131516-7061-4be8-a33b-493a21b857bb)
Run the app:
![image](https://github.com/user-attachments/assets/8e3acaef-ab8b-47ff-bd6d-8e1f5c9437c5)
Open in browser:
![image](https://github.com/user-attachments/assets/da8d193c-2fff-4a04-8dde-00835f7da155)
✨ Future Enhancements
✅ PDF export of journal logs

✅ Spotify mood-based playlist integration

✅ Emotion classification using deep learning

⏳ Dark mode UI

⏳ Progress tracking dashboard

🤝 Contributing
Feel free to fork, enhance, and raise issues. Mental health matters — let’s make tech accessible and supportive.


