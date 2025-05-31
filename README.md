🌿 MoodMate – Your AI Mental Health Companion
![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/flask-%5E2.0-blue) ![Status](https://img.shields.io/badge/status-active-brightgreen)
MoodMate is a personalized AI-powered wellness assistant that helps users track their emotions, journal feelings, and receive curated Spotify music recommendations based on their mood. Built using NLP, PyTorch, Flask, and Spotify API, MoodMate provides a safe and interactive space to care for mental health.
🧠 Features
•	💬 Emotion-Aware Chatbot trained on mental health-related conversations
•	🎵 Spotify Integration for mood-based song/playlist suggestions
•	📓 Guided Journaling with emotional prompts and downloadable entries
•	📊 Mood Tracking (optional MongoDB integration)
•	🌐 Web-Based Interface using Flask and HTML/CSS
📁 Project Structure

MoodMate/
├── app1.py                 # Flask backend server
├── chat.py                 # Chat logic and NLP model inference
├── train.py                # Model training script using PyTorch
├── model.py                # Feedforward neural network definition
├── nltk_utils.py           # Tokenization, stemming, bag-of-words functions
├── intents.json            # Predefined intents with emotional tone
├── data.pth                # Trained PyTorch model
├── templates/
│   └── index.html          # Frontend UI template
├── screenshots/            # Project screenshots
├── nltk_data/              # Required NLTK corpora
├── .env                    # API keys (Spotify)
└── requirements.txt        # Python dependencies

🚀 Getting Started
1.	1. Clone the Repository
git clone https://github.com/yourusername/MoodMate.git
cd MoodMate
2.	2. Set Up Virtual Environment & Install Dependencies
python -m venv venv
venv\Scripts\activate  # On Windows
# or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
3.	3. Train the Model
python train.py
4.	4. Run the App Locally
python app1.py
Visit http://127.0.0.1:5000 in your browser to start chatting!
🔐 Spotify API Integration
1. Go to Spotify Developer Dashboard: https://developer.spotify.com/dashboard
2. Create a new app and note your Client ID and Client Secret
3. Add them to your `.env` file:
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
Spotify will now return playlists based on emotion detected during conversations.
📝 Sample Journaling Prompts
•	What's been weighing on your mind lately?
•	Describe a moment that brought you peace.
•	What advice would you give your past self today?
🗂 Journals are auto-saved and available for download as `.txt` or `.pdf`.
🧪 Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask), PyTorch
Database: Optional MongoDB for mood tracking
Integrations: Spotify Web API
