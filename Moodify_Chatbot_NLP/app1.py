from flask import Flask, render_template, request, jsonify
from chat import get_response  # Your trained chatbot logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    response = get_response(data["message"])
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
