#!/usr/bin/python
import sys
import os
from os import environ
import sqlite3
import time
import os.path
from os import path

form = open("/home/student/zhangs22/public_html/info.html").read()

not_done = True
while (not_done):
	while path.exists("lock.txt"):
		time.sleep(2)

	f = open("lock.txt", "a")
	myPid = str(os.getpid())
	f.write(myPid)
	f.close()

	f = open("lock.txt", "r")
	pid = f.read()
	if pid == myPid:
		not_done = False

print "Content-type: text/html\n"

form_values = {}
if os.environ["REQUEST_METHOD"] == "POST":
	for line1 in sys.stdin:
		print line1
		line1 = line1.replace('\n', "")
		form_values_str = line1.split('&')

		for i in form_values_str:
			# print i
			parts = i.split("=")
			key = parts[0]
			val = parts[1]
			# print val
			form_values[key] = val 

# print form_values
note_value = form_values['note_id']

for line in sys.stdin:
	new_line = line.split('=')[1]
	print new_line

connection = sqlite3.connect("db.txt")

connection.execute('delete from notes where note_id=?', (note_value,))

connection.commit()

os.remove("lock.txt")

print "Location: ./login.cgi\n\n",