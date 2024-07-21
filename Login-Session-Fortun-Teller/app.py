from flask import Flask, render_template,request,redirect,url_for, session as login_session
import random

app = Flask(__name__, template_folder='templates', static_folder="static")
app.config['SECRET_KEY'] = "amir"


@app.route('/', methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login_page.html")
	else:
		name = request.form['first_name']
		birth_date = request.form['birth_date']

		login_session['name'] = name
		login_session['birth_date'] = birth_date
		return redirect(url_for("home"))

# Route for the home page
@app.route('/home', methods=["GET","POST"])
def home():
	name = login_session.get('name')
	birth_date = login_session.get('birth_date')

	birth_month_length = len(birth_date)
	if request.method == "GET":
	    return render_template("home.html", name=name , birth_date=birth_date, birth_month_length=birth_month_length)
	else:	        
		# if birth_date:
		# 	birth_month_length = len(birth_date)
		# 	return redirect(url_for('fortune', birth_month_length=birth_month_length))
		return redirect(url_for(''))

fortunes = ["Your creativity will lead you to great success.",
			"A thrilling adventure awaits you in the near future.",
			"An unexpected financial gain is coming your way.",
			"Your kindness will bring you unexpected blessings.",
			"Embrace change with an open heart and mind.",
			"A long-lost friend will re-enter your life soon.",
			"Trust your instincts; they will guide you wisely.",
			"Good news will come to you from far away.",
			"Take a risk; it will pay off handsomely.",
			"Today is a great day to tackle a new challenge."
]


@app.route('/fortune/<int:birth_month_length>' , methods=["GET","POST"])
def fortune(birth_month_length):

	if birth_month_length < 10 :
		random_fortune_text = fortunes[birth_month_length]
		login_session['fortune'] = random_fortune_text
	
		# random_number = random.randint(0,9)
		return render_template('fortune.html', random_fortune = random_fortune_text, birth_month_length=birth_month_length)
	else :
		random_fortune_text = "You have a bad fortune"
		login_session['fortune'] = random_fortune_text
		return render_template('fortune.html', random_fortune= random_fortune_text)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)