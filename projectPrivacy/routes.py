from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("/index.html")

@app.route("/navigation")
def navigation():
	# When x is equal to True it means the user is logged in. 
	# Havent setup the login pages yet. 
	# Currently just manually toggling the x value.
	x = True
	if x == True:
		return render_template("/navigation.html", x = True)
	elif x == False:
		return render_template("/navigation.html", x = False)
	
@app.route("/login")
def login():
	return render_template("/login.html")
	
# For when the forms are working
# @app.route("/help", methods=['GET', 'POST'])

# For now
@app.route("/help")
def help():
	return render_template("/help.html")
	
# Stuff for forms: Not working	
	# form = HelpForm()
	
	#if request.method == 'POST':
	#	return "Success!"
	#elif request.method == 'GET':
	#	return render_template("/help.html", form = form)
	
if __name__ == "__main__":
	app.run(debug=True)