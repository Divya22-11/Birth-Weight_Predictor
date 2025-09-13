'''
#                                    import flask
from flask import Flask

#                                   create flask instance
app = Flask(__name__)

#                                   define function and route
@app.route('/')
def home():
    return("hello world")

#                                       trigger the flask app
if __name__ == '__main__':
    app.run()
    
'''
from flask import Flask

app=Flask(__name__)

@app.route("/")
def fun():
    return("I am doing flask operations")

if __name__ == '__main__':
    app.run()

