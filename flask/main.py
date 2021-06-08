from flask import Flask,render_template, request
import smtplib, ssl

# initialise flask
app = Flask(__name__) 

# routes
@app.route("/")
def index():
	return render_template("index.html")

# to check errors

@app.route("/result", methods = ["GET", "POST"])
def result():
	if(request.method == "POST"):
		sender = request.form.get("sender")
		password = request.form.get("password")
		reciever = request.form.get("reciever")
		message = request.form.get("message")
		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server.login(sender, password)
		server.sendmail(sender, reciever, message)
		""" with smtplib.SMTP("smtp.gmail.com", 465) as connection:
			# securing connection
			connection.starttls()
			connection.login(user=sender, password=password)
			connection.sendmail(
				from_addr=sender,
				to_addrs=reciever,
				msg="Subject : Hello\n\n\n\nThis is the body of my email"
			) """
	return render_template("result.html")

app.run(debug = True)

""" my_email = "john@gmail.com"
password = "abc"
with smtplib.SMTP("smtp.gmail.com") as connection:
    # securing connection
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="abc@gmail.com",
        msg="Subject : Hello\n\n\n\nThis is the body of my email"
    )
"""