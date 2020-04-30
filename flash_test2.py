import datetime 
from flask import Flask , render_template
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1

    names = ["alice","Bob","joghe"]

    return render_template('index.html',names = names)

@app.route('/more')
def more():
    return render_template('more.html')

if(__name__ == '__main__'):
    app.run()
