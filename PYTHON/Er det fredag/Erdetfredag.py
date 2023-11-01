from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello_world():
    today = datetime.today()
    day_of_week = today.weekday()
    if day_of_week == 0:
        day = 'mandag'
    elif day_of_week == 1:
        day = 'tirsdag'
    elif day_of_week == 2:
        day = 'onsdag'
    elif day_of_week == 3:
        day = 'torsdag'
    elif day_of_week == 4:
        day = 'fredag'
    elif day_of_week == 5:
        day = 'lørdag'
    elif day_of_week == 6:
        day = 'søndag'
    return render_template('index.html', date=day)

if __name__ == '__main__':
    app.run()