from flask import Flask, render_template, url_for

app = Flask(__name__)

projects_list ={
        'tkMarker: A Markdown editor using tkinter': 'https://github.com/GordonZhang2024/tkMarker/',
        'GordonZhang2024/website: The source files of this website': 'https://github.com/GordonZhang2024/website/'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects_list=projects_list)

