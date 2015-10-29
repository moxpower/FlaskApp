#http://localhost:5000

from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/index')
def index():
    user = {'nickname':'moxpower'}
    return render_template('index.html',
                           title='Home',
                           user=user)

if __name__ == '__main__':
    app.run()