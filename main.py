import pickle 
from flask import Flask,request,app, jsonify, render_template 
import numpy as np 
import pandas as pd 

app=Flask(__name__) 

model=pickle.load(open('knn_pkl','rb')) 

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/predict_api', methods=['post']) 
def predict_api(): 
    data=request.json['data'] 
    print(data)
    input=np.array(list(data.values())).reshape(1,-1) 
    output=model.predict(input) 
    print(output[0]) 
    return jsonify(output[0]) 

@app.route('/predict', methods=['POST'])
def predict():
    input=[float(x) for x in request.form.values()]
    # gets the inputs from the submitted form's values. 


    input_array = np.array(input).reshape(1, -1)
    df = pd.DataFrame(columns=request.form.keys(), data=input_array)
    # reshapes the array of the inputs into a format the model can understand. 
    output=str(model.predict(df)[0])

    # makes the prediction of the inputs passed in with the model. 
    return render_template("home.html", prediction_test=output)


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")