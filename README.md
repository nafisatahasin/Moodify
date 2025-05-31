
# 💬 Moodify – Your AI Wellness Companion 🧠🎧

**Moodify** is an intelligent mental health chatbot that supports emotional well-being through empathetic conversations, mood-based Spotify music, and reflective journaling prompts. Built using **Flask**, **PyTorch**, and **NLP**, Moodify offers a safe and calm space for users to talk and feel heard.

---

## 🌟 Features

- 🧘 Understands emotional input using natural language processing.
- 🎧 Suggests **Spotify playlists** based on your mood.
- 📝 Offers **journaling prompts** for self-reflection.
- 🧠 Trained on custom intents and emotional patterns.
- 💻 Web + CLI versions available.

---

## 🛠️ Tech Stack

- **Backend:** Flask + PyTorch
- **Frontend:** HTML, CSS, JS
- **NLP:** Custom model using bag-of-words and tokenization
- **Music API:** Spotify (via Spotipy)
- **Hosting-ready:** Easily deploy on Heroku, Render, etc.

---

## 🧑‍💻 Setup Instructions

### 📦 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Moodify.git
cd Moodify
```

### 📂 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 🔧 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Setup Spotify Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an app and get your:
   - `Client ID`
   - `Client Secret`
3. Create a `.env` file in the root directory:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

---

### ▶️ 5. Run the Web App

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 💬 Try the CLI Chatbot

```bash
python chat.py
```

---

## 📁 Project Structure

```
Moodify/
│
├── templates/
│   └── index.html            # Frontend interface
├── static/                   # CSS, JS, assets
├── intents.json              # Chatbot training data
├── model.py                  # PyTorch model
├── nltk_utils.py             # NLP processing tools
├── app.py                    # Flask app with Spotify integration
├── chat.py                   # CLI-based chatbot
├── data.pth                  # Trained model file
├── requirements.txt
└── .env                      # Spotify credentials (not committed)
```

---

## 🎯 Future Ideas

- 📱 Mobile support / responsive UI
- 📊 Analytics dashboard (e.g., mood over time)
- 🔒 Authentication for personalized journaling
- 🌈 Voice input integration

---

## 🙌 Contributions

Pull requests and suggestions are welcome! 

---

## 💖 Made with care to support mental health 💖
