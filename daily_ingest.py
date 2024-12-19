"""
Pull the day's wordle answer
and append to list of words

Author: lauram93@gmail.com
Date:   2024-Jun-07
"""
from datetime import date, timedelta
import requests

def get_todays_word():
    today = date.today()-timedelta(1)
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        wordle_answer = response.text.strip()
        with open("wordle_answers.txt", "a") as file:
            file.write(wordle_answer + "\n")

def main():
    get_todays_word()

if __name__ == "__main__":
    main()