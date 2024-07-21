from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder="static")
app.config['SECRET_KEY'] = "amir"

firebaseConfig = {
  "apiKey": "AIzaSyAAQtVaOWfLv3uRu4eZcm1GQkDVcUOCuMI",
  "authDomain": "auth-lab-bde4f.firebaseapp.com",
  "projectId": "auth-lab-bde4f",
  "storageBucket": "auth-lab-bde4f.appspot.com",
  "messagingSenderId": "637759847224",
  "appId": "1:637759847224:web:8d027e8faf2c02e3c55fcd",
  "measurementId": "G-CHTJKMJ7DF",
  "databaseURL": ""
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


@app.route("/", methods = ["GET", "POST"])
def main():
	if request.method == "GET":
		return render_template("signup.html")

	email = request.form['email']
	password = request.form['password']

	# login_session['email'] = email
	# login_session['password'] = password
	# login_session['quotes'] = []
	try:
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		login_session['quotes'] = []
		return redirect(url_for('home'))
			
	except:
		return ("error creating account")


@app.route("/signout", methods = ["GET", "POST"])
def signout():
	login_session['user']= 	None
	auth.current_user = None
	print("signed out user")
	return redirect(url_for('signin'))	


@app.route("/signin", methods = ["GET", "POST"])
def signin():
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			print(auth.create_user_with_email_and_password(email, password))
			return redirect(url_for('signin'))
		except:
			error = "Authentication failed"
			print(error)
			return render_template("signup.html")


@app.route("/home", methods = ["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template('home.html')
	else :
		quote = request.form['quote']
		login_session['quotes'].append(quote)
		login_session.modified = True
		return render_template('thanks.html')

@app.route("/thanks", methods = ["GET", "POST"])
def thanks():
	return render_template("thanks.html")

@app.route("/display", methods = ["GET", "POST"])
def display():
	return render_template("display.html", quotes=login_session['quotes'])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)