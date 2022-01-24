from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
	getmail = request.args.get('getmail')
	getpass = request.args.get('getpass')
	subjek = request.args.get('subjek')
	kirimke = request.args.get('tomail')
	text = request.args.get('text')
	app.config['MAIL_USERNAME'] = getmail
	app.config['MAIL_PASSWORD'] = getpass
	mail = Mail(app)
	msg = Message(subjek, sender = getmail, recipients = [kirimke])
	msg.body = text
	mail.send(msg)
	return "Sent"

if __name__ == '__main__':
	app.run(debug = True)
