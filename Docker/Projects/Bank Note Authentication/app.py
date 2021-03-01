from flask import Flask, app,request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)



@app.route('/')
def welcome():
    return "Welcome Home"
# http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis&entropy=1
# http://127.0.0.1:5000/predict_file?file=TestFile.csv
@app.route('/predict')
def predict_note_authentication():
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
   df_test=pd.read_csv(request.files.get("file"))

   prediction=classifier.predict(df_test)


   return "The Prediction Values for the csv is "+ str(list(prediction))




if __name__=="__main__":
    app.run(debug=True)