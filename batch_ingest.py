# """
# Batch ingest Wordle answers between two dates
# and write to text file. Should only be run once to 
# generate the file, and then every day thereafter
# append that day's answer with daily_ingest.py
#
# Author: lauram93@gmail.com
# Date:   2024-Jun-07
# """
from datetime import datetime, timedelta
import requests

def batch_ingest():
    start_date = datetime.strptime('2021-06-19', '%Y-%m-%d')
    end_date = datetime.today()

    current_date = start_date
    while current_date <= end_date:
        #print(current_date.strftime('%Y-%m-%d'))
        url = f"https://www.nytimes.com/svc/wordle/v2/{current_date.strftime('%Y-%m-%d')}.json"
        print(url)
        current_date += timedelta(days=1)

        response = requests.get(url)
        if response.status_code == 200:
            wordle_answer = response.text.strip()
            with open("wordle_answers.txt", "a") as file:
                file.write(wordle_answer + "\n")

def main():
    batch_ingest()

if __name__ == "__main__":
    main()