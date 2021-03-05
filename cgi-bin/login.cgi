#!/usr/bin/python
import sys
import os
from os import environ
import sqlite3
import os.path
from os import path

print "Content-type: text/html" + "\n",

username = None

if os.environ["REQUEST_METHOD"] == "POST":
	for line1 in sys.stdin:
		first_word = line1.split('&')[0]
		username = first_word.split('=')[1]

if username is not None:
	print "Set-Cookie: " +  "user=" + username + "\n",

	# http response needs to have this newline between headers and body
	print "\n"

	print "Hi, " + username + "<br>"

print "\n"

if username is None:
	if os.environ.get("HTTP_COOKIE") is not None:
		cookie = os.environ["HTTP_COOKIE"]
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
		username = cookie_values["user"]
		print "Loading user from cookie: " + username
	else:
		print "Not logged in (no form submitted and no existing cookie)"

connection = sqlite3.connect("db.txt")

form = open("/home/student/zhangs22/public_html/info.html").read()
#form = open("info.html").read()

print form

print "Hi, " + username

print "Here are your notes: "

connection = sqlite3.connect("db.txt")

for row in connection.execute("select note_id, owner, note from notes where owner=?", (username,)):
    # this returns a tuple with 2 pieces
    print "<br>"
    print("Hi, my id is {} my name is {} and I said >{}<".format(row[0], row[1], row[2]))


