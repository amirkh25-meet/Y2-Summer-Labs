from flask import Flask, render_template,request,redirect,url_for
import random

app = Flask(__name__, template_folder='templates', static_folder="static")

# Route for the home page
@app.route('/home', methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        birthday = request.form["birthday"]
        birth_month_length = len(birthday) 
        # print(birth_month_length)
        return redirect(url_for("fortune", birth_month_length=birth_month_length))


fortunes = ["Your creativity will lead you to great success.",
			"A thrilling adventure awaits you in the near future.",
			"An unexpected financial gain is coming your way.",
			"Your kindness will bring you unexpected blessings.",
			"Embrace change with an open heart and mind.",
			"A long-lost friend will re-enter your life soon.",
			"Trust your instincts; they will guide you wisely.",
			"Good news will come to you from far away.",
			"Take a risk; it will pay off handsomely.",
			"Today is a great day to tackle a new challenge."]


@app.route('/fortune/<int:birth_month_length>')
def fortune(birth_month_length):
	if birth_month_length < 10 :
		random_fortune_text = fortunes[birth_month_length]
		# random_number = random.randint(0,9)
		return render_template('fortune.html', random_fortune = random_fortune_text, fortunes = fortunes,birth_month_length=birth_month_length)
	else :
		return render_template('fortune.html', random_fortune="You have a bad fortune")


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)