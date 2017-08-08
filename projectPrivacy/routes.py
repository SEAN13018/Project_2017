from flask import Flask, url_for, render_template, request, redirect, session
from flask.ext import login as flask_login
import sqlite3 as sql
#import email                            a python file. 

app = Flask(__name__)

#need to tidy this up put in a separate python file. 
#from http://gatherworkshops.github.io/digital-information/courses/web-data-with-sqlite/ (a tutorial)

app.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
	
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.authenticated = False
		
	def get_id(self):
		return self.username
		
	def is_authenticated(self):
		return self.authenticated
		
	def is_active(self):
		return true

@app.route("/")
def index():
	return render_template("/index.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('/login.html')
	elif request.method == 'POST':
		username = request.form['username']
		passw = request.form['password']
		
		#Stuff for login goes here

@app.route("/navigation")
def navigation():
	# When x is equal to True it means the user is logged in. 
	# Havent setup the login pages yet. 
	# Currently just manually toggling the x value.
	x = False
	if x == True:
		return render_template("/navigation.html", x = True)
	elif x == False:
		return render_template("/navigation.html", x = False)

		
# A simple form is on the help page.	
@app.route("/help", methods = ['GET', 'POST'])
def help():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		query = request.form['query']
			
		con = sql.connect("database.db")
		cur = con.cursor()
		cur.execute("INSERT INTO help (firstname, lastname, email, query) VALUES (?,?,?,?)", (firstname, lastname, email, query))
		con.commit()
		con.close()
		return render_template("result.html")

	elif request.method == 'GET':
		return render_template("/help.html")
	
if __name__ == "__main__":
	app.run(debug=True)