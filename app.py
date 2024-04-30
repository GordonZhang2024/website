from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)

projects_list = {
        'tkMarker | A Markdown editor': ' https://gordonzhang.pythonanywhere.com/projects/tkMarker/',
        'GordonZhang2024/website | The source files of this website': 'https://github.com/GordonZhang2024/website/',
        'xss shield | A python library which is used to stop your website from being attacked.': 'https://pypi.org/project/xss-shield/'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects_list=projects_list)

@app.route('/projects/tkMarker/')
def tkmarker():
    return render_template('tkmarker.html')

@app.route('/robots.txt')
def robotstxt():
    return send_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_file('sitemap.xml')
    
