from flask import Flask
import datetime



app = Flask(__name__)

@app.route('/time')
def display_countdown():
    today = datetime.datetime.now()
    end_day = datetime.datetime(2021, 1, 1, 0, 0, 0)
    difference = end_day - today
    return f"the countdown to january 1st is {difference}"

if __name__ == "__main__":
    app.run()