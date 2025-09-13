import pickle

import pandas as pd
from flask import Flask, jsonify, render_template, request

app=Flask(__name__)

def get_cleaned_data(form_data):
    gestation=float(form_data["gestation"])
    parity=int(form_data["parity"])
    age= float(form_data["age"])
    height= float(form_data["height"])
    weight= float(form_data["weight"])
    smoke= float(form_data["smoke"])
   
    cleaned_data={
        "gestation":[gestation],
        "parity" : [parity],
        "age": [age],
        "height":[height],
        "weight":[weight],
        "smoke":[smoke ]   }
    
    return cleaned_data

@app.route("/",methods=["GET"])
def home_page():
    return render_template("birth_weight.html")

# define end point
@app.route("/predict",methods=["POST"])
def get_prediction():
    #make request to get your data:
    baby_data_form = request.form
    
    baby_data_cleaned = get_cleaned_data(baby_data_form)
    
    
    # convert into data frame:
    baby_df = pd.DataFrame(baby_data_cleaned)
    
    
    # load a Ml trained model:
    with open("model/model.pkl","rb") as obj:
        model=pickle.load(obj)
        
    # make prediction on user data:
    prediction = model.predict(baby_df)
    
    # prediction is created in a vairable(prediction):
    prediction = round(float(prediction),2)
    
    
    #returb response in json format:
    response= {"Prediction":prediction}
    return render_template("predict.html",prediction = prediction)
        


if __name__== ("__main__"):
    app.run(debug=True)