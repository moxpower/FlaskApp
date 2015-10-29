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
    posts = [
        {
            'author': {'nickname':'John'},
            'question': 'How many regression models exist in machine learning?',
            'answer':'<a href=http://www6.in.tum.de/Main/TeachingWs2009MachineLearning>Check class</a>'
        },
        {
            'author': {'nickname':'Susan'},
            'question': 'How many lines of code in R do you need for a linear regression?',
            'answer':'4?'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

if __name__ == '__main__':
    app.run()