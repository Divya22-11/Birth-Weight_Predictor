# 1. import Flask
# 2. instance of Flask
# 3. make function and route 

#url:

# base url > further parts
#"/","/about","/data"


# 4. trigger the flask app



from flask import Flask, jsonify, render_template

app = Flask(__name__)

# @app.route("/")
# def base():
#     return("Welcome to my website")

@app.route("/about")
def about():
    return"""<h1>About us</h1><br>
            <h2>In this website you gonna see about the Data Analytics.</h2><br>
            <h3>Thank You for visiting.</h3>"""
    
    
@app.route("/data")
def data():
    user_data={"Name":"Divya",
            "Age": 20,
            "Course":"DA"}
    return jsonify(user_data)

#>>>>>>>>>>>>>> how to connect html with python code:  render_template

# @app.route('/')
# def home_page():
#     name="Bhanu"
#     return render_template('index.html',name=name)

# @app.route("/",methods=["GET"])   >>>>> we use method to get output
# def home():
#     return "hello world"

@app.route("/" , methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/form",methods=["POSt"])
def welcome():
    return ("we have recieved your information")


if __name__== "__main__":
    app.run(debug= True)   # debug > it will change the data in website by just saving this file