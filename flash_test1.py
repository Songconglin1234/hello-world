import datetime 
from flask import Flask , render_template
from flask import request

app = Flask(__name__)
@app.route('/helloworld')
def hello_world():
    return("hello world")

@app.route('/get.html')
def get_html():
    return render_template('get.html')

@app.route('/post.html')
def post_html():
    return render_template('post.html')

@app.route('/deal_request',methods = ['GET','POST'])
def deal_request():
    if(request.method == 'GET'):
        get_q = request.args.get("q","")
        return render_template("result.html",result = get_q)
    elif request.method == 'POST':
        post_q = request.form["q"]
        return render_template("result.html",result = post_q)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)