from flask import Flask, app,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger



app=Flask(__name__)
Swagger(app)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)



@app.route('/')
def welcome():
    return "Welcome Home"
# http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis&entropy=1
# http://127.0.0.1:5000/predict_file?file=TestFile.csv
@app.route('/predict')
def predict_note_authentication():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    # print(variance,skewness,curtosis,entropy)

    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    # print(prediction)

    return "The Prediction Value is "+ str(prediction[0])

@app.route('/predict_file',methods=['POST'])
def predict_note_file_authentication():

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))

    prediction=classifier.predict(df_test)


    return "The Prediction Values for the csv is "+ str(list(prediction))




if __name__=="__main__":
    app.run(debug=True)