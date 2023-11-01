from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/huntingSimulator')
def huntingSimulator():
    return render_template('huntingSimulator.html')


def cookie():
    webbrowser.open('https://orteil.dashnet.org/cookieclicker/')

if __name__ == '__main__':
    app.run(debug=True)
