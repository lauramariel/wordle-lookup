Uses the NYTimes API: https://www.nytimes.com/svc/wordle/v2/YYYY-MM-DD.json

Install requirements
```
pip install -r requirements.txt
```

Generate list of Wordle answers
```
python3 batch_ingest.py
```

Run Flask
```
flask run
```

Example usage once API is up and running
```
$ curl -X POST http://localhost:5000/check-word -H "Content-Type: application/json" -d '{"word":"party"}'
{"date":"2023-08-03","exists":true}
$ curl -X POST http://localhost:5000/check-word -H "Content-Type: application/json" -d '{"word":"ether"}'
{"date":"2024-06-06","exists":true}
```

Todo
- Set a scheduler to add to wordle_answers.txt daily with daily_ingest.py
- Create a front end