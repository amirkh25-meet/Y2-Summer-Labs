from flask import Flask, render_template
import random

app = Flask(__name__)

# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/fortune')
def fortune():
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
	random_number=random.randint(0,10)
	random_fortune_text = fortunes[random_number]
	return render_template('fortune.html', random_fortune = random_fortune_text	)



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)