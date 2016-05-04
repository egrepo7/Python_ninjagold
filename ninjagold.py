from flask import Flask, render_template, request, session, redirect
app = Flask (__name__)
app.secret_key = 'secretz'
import random, datetime

@app.route('/')
def index():
	now = datetime.datetime.now()
	tformat = "%a %b %d, %Y %H:%M:%S"
	newTime = now.strftime(tformat)
	session['time'] = newTime
	
	if "score" not in session:
		session['gold'] = 0
	if "text" not in session:
		session['text'] = []
	return render_template('main.html')

@app.route('/process_gold', methods = ['POST'])
def getmoneyz():
	if request.form['action'] == "farm":
		session['newgold'] = random.randint(10, 20)
		session['gold'] += session['newgold']
		session['text'].insert(0, "You have taken " + str(session['newgold']) + " gold from the farm!.. Poor cows :( - " + session['time'])
	elif request.form['action'] == "cave":
		session['newgold'] = random.randint(5,10)
		session['gold'] += session['newgold']
		session['text'].insert(0, "You have taken " + str(session['newgold']) + " gold from the cave! ...You've angered the ogres! - " + session['time'])
	elif request.form['action'] == "house":
		session['newgold'] = random.randint(2,5)
		session['gold'] += session['newgold']
		session['text'].insert(0, "You have taken " + str(session['newgold']) + " gold from someone's house! ...Thief! - " + session['time'])
	else:
		session['newgold'] = random.randint(-50,50)
		session['gold'] += session['newgold']
		if session['newgold'] > 0:
			session['text'].insert(0, "You have won " + str(session['newgold']) + " gold from the casino!.. BIG MONEYZ! + " + session['time'] )
		else:
			session['text'].insert(0, "You have lost " + str(session['newgold']) + " gold from the casino!... Time to go home... - " + session['time'])


	return render_template('main.html')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

# @app.route('/process_money', methods = ['POST'])
# def moneyz();

app.run(debug=True)