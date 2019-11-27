from flask import Flask
app = Flask(__name__)

import datetime

@app.route("/")
def hello():
	print("Hello World!")
	now = datetime.datetime.now()
	print ("Current date and time is ")
	print (now.strftime("%A, %d-%m-%Y : %H:%M"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




