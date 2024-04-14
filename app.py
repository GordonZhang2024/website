from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/tkMarker')
def tkmarker():
    return render_template('tkMarker/index.html')
