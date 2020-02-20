from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def time():
    today = datetime.datetime.now()
    hour = today.hour

    if hour > 8 and hour < 13:
        return "Good Morning"
    elif hour > 13 and hour < 17:
        return "Good Afternoon"
    elif hour > 17 and hour < 21:
        return "Good evening"
    else:
        return "Good Night"




if __name__ == "__main__":
    app.run()
