import os
from twilio.rest import Client
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", content="Testing")
 
@app.route("/sms", methods=["POST", "GET"])
def sms():
    if request.method == "POST":

        tonum = request.form["smsnum"]
        tobody = str(request.form["smsbody"])
        account_sid = 'AC46648a764504d96ef5f6ff9d7c493117'
        auth_token = '11eb94b229fa1348c2ce5fe730254d4c'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=tobody,
                            from_='+19035002648',
                            to=tonum
                        )

        print(message.sid)
        print(message.body)
        return("sms sent")
    else:
        return render_template("sms.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

