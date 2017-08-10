from flask import url_for, render_template, request, redirect, session, g
import sqlite3 as sql
from public import website
from public import usermanager
from public import datamanager
from flask_login import current_user

#from public import email
# ^a python file for when I have coded the email file...

# Use a tutorial from https://pythonprogramming.net/password-hashing-flask-tutorial/
# For encrypting passwords...

@website.route("/")
def index():
	return render_template("/index.html")

@website.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		if current_user.is_authenticated:
			return render_template('/index.html')
		else:
			return render_template('/login.html')
	
	elif request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		
		user = usermanager.sign_in_user(username, password)
		if current_user.is_authenticated:
			return redirect('/')
		else:
			return render_template('/login.html')
	
@website.route("/navigation")
def navigation():
	# If the user is logged in it will show navigation for messaging and signing out. 
	if current_user.is_authenticated:
		return render_template("/navigation.html", x = True)
	else:
		return render_template("/navigation.html", x = False)

		
# A simple form is on the help page.	
@website.route("/help", methods = ['GET', 'POST'])
def help():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		query = request.form['query']
			
		con = sql.connect("project.db")
		cur = con.cursor()
		cur.execute("INSERT INTO help (firstname, lastname, email, query) VALUES (?,?,?,?)", (firstname, lastname, email, query))
		con.commit()
		con.close()
		return render_template("result.html")

	elif request.method == 'GET':
		return render_template("/help.html")
		
@website.route('/signout')
def sign_out():
	usermanager.sign_out_user()
	return render_template('signout.html')