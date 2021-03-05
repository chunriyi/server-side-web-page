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

# GET /login.html HTTP/2.0
# Host: http://www-test.cs.umanitoba.ca/~zhangs22/login.html
# Cookie: user=test123

for line in sys.stdin:
	new_line = line.split('=')[1]
	print new_line

cookie = os.environ ["HTTP_COOKIE"]
# print cookie

cookies = cookie.split(";")

cookie_values = {}
for i in cookies:
	# print i
	parts = i.split("=")
	key = parts[0]
	val = parts[1]
	# print val
	cookie_values[key] = val 

# print cookie_values
# print "user=" + cookie_values["user"]

connection = sqlite3.connect("db.txt")

name = cookie_values["user"]

connection.execute("insert into notes(owner, note) values (?,?)", (name, new_line))

connection.commit()

os.remove("lock.txt")

print "Location: ./login.cgi\n\n",