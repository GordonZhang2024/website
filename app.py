from flask import Flask, render_template, url_for, send_file
from MySQLdb import *
from passwd import db_passwd  # Set your password as db_passwd in passwd.py

db = connect('GordonZhang.mysql.pythonanywhere-services.com', 'GordonZhang', db_passwd, 'GordonZhang$website')
cursor = db.cursor()

cursor.execute('SELECT * FROM projects')
projects_list = cursor.fetchall()
projects = list(projects_list)
lenth = len(projects_list)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects_list=projects_list, lenth=lenth)

@app.route('/projects/tkMarker/')
def tkmarker():
    return render_template('tkmarker.html')

@app.route('/robots.txt')
def robotstxt():
    return send_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_file('sitemap.xml')


@app.errorhandler(404)
def pagenotfound(arg):
    return render_template('404.html'), 404
