from flask import Flask, Response, jsonify
from flask_cors import CORS  # Import CORS from flask_cors


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/")
def home():
    return "This is my First App"

@app.route("/user-details/<Id>")
def user_Details(Id):
    Data={
        "id":Id,
        "Name":"Muhammad Jawad",
        "Age":"27"
    }

    return jsonify(Data),200

if __name__=="__main__":
    app.run(debug=True)


