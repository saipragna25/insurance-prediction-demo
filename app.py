from flask import Flask, request, render_template
import pandas as pd
import pickle
from flask_cors import CORS
#from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# file = open("xgb.pkl", 'rb')
# model = xgboost.XGBRegressor()
# model.load_model("xgb2.json")
model = pickle.load(open("linear.pkl", 'rb'))

# data = pd.read_csv('./clean_data.csv')
# data.head()

@app.route('/')
def index():
    
    return "<h1>Hello </h1>"
gender_map = {"male" : 0,
                     "female" : 1}
smoker_map = {"no":0,"yes":1}
region_map = {"northwest":1,"northeast":2,"southwest":3,"southeast":4}
@app.route('/predict', methods=['POST'])
def predict():
    print("request")
    print(request)
    age = int(request.form.get('age'))
    sex = gender_map[request.form.get('sex')]
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = smoker_map[request.form.get('smoker')]
    region = region_map[request.form.get('region')]
    print(age,sex,bmi,children,smoker,region)

    prediction = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]], 
                columns=["age","sex","bmi","children","smoker","region"]))
    print(prediction)
    return str(prediction[0])           
    #return "hi"

if __name__=="__main__":
    app.run(debug=True)
