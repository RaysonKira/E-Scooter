from flask import Flask, redirect, request, url_for, render_template
from firebase import firebase

app = Flask(__name__)
app.config.from_object(__name__) # consume the configuration above

firebase = \
    firebase.FirebaseApplication('https://mynotawesomeproject-81927.firebaseio.com/', None)

@app.route('/E-Scooter')
def EScooter():
    return render_template("MainR.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

# decorator which tells flask what url triggers this fn
@app.route('/messages')
def messages():
  result = firebase.get('/messages', None)
  return render_template('list.html', messages=result)

@app.route('/submit_message', methods=['POST'])
def submit_message():
  message = {
    'body': request.form['message'],
    'who': request.form['who']
  }
  firebase.post('/messages', message)
  return redirect(url_for('messages'))

#for user to get the login informations



if __name__ == '__main__':
    app.run(debug=True)

