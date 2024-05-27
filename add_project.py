#!/usr/bin/env python

from MySQLdb import *
from passwd import *


db = connect('GordonZhang.mysql.pythonanywhere-services.com', 'GordonZhang', db_passwd, 'GordonZhang$website')
cursor = db.cursor()

name = input('Enter project name: ')
url = input('Enter project url: ')

command = f'INSERT INTO projects VALUES ("{name}", "{url}")'

cursor.execute(command)

print("Projects list updated")

db.commit()
