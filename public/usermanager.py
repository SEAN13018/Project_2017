from public import website
import flask_login
from flask_login import login_required

website.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()
login_manager.init_app(website)

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
		
login_manager.login_view = "login" 

def sign_in_user(username, password): # is this in the right place?
	
	user = load_user(username)
		
	if user and user.password == password:
		user.authenticated = True
		flask_login.login_user(user)
		
	return flask_login.current_user
	

@login_manager.user_loader
def load_user(username):
	return None