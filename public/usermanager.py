from public import website
from public import datamanager
from flask.ext import login as flask_login
from flask_login import login_required

website.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()
login_manager.init_app(website)

login_manager.login_view = "login" 

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
		return True
		
	def is_anonymous(self):
		return False

def sign_in_user(username, password):
	
	user = load_user(username)
		
	if user and user.password == password:
		user.authenticated = True
		flask_login.login_user(user)
		
	return flask_login.current_user
	

@login_manager.user_loader
def load_user(username):
	query_string = (
		'SELECT uid, username, password FROM users WHERE username =	 ?'
	)
	
	query_result = datamanager.query_db(query_string, [username], one=True)
	
	if query_result == None:
		return None
		
	else:
		user = User(
			query_result['username'],
			query_result['password']
		)
		
		user.id = query_result['uid']
		
		return user