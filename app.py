"""
API to check a word against the list of Wordle answers

Author: lauram93@gmail.com
Date:   2024-Jun-07
"""
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def load_wordle_answers():
    with open("wordle_answers.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/check-word", methods=["POST"])
def check_word():
    data = request.get_json()
    word = data.get("word")
    wordle_answers = load_wordle_answers()

    found = 0 
    for answer in wordle_answers:
        # wordle_answers is a list of strings in dict format
        # e.g. {"id":1091,"solution":"party","print_date":"2023-08-03","days_since_launch":775,"editor":"Tracy Bennett"}
        if word in json.loads(answer).get("solution"):
            # found it
            print_date = json.loads(answer).get("print_date")
            found = 1

    if found == 1:
        return jsonify({"exists": True, "message": f"This word was used in Wordle on {print_date}"})
    else:
        return jsonify({"exists": False, "message": "This word has not been used in Wordle yet"})

if __name__ == "__main__":
    app.run(debug=True)