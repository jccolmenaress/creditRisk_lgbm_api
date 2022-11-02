from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import xgboost as xgb
import lightgbm as lgb
from lightgbm import LGBMClassifier
import joblib
#from lightgbm import LGBMClassifier

app = FastAPI()

class model_input(BaseModel):
    #asi sabe la api el formato de datos que necesita
    Seniority: float
    Time : float
    Age : float
    Expenses : float
    Income : float
    Assets : float
    Debt : float
    Amount : float
    Price : float
    Home_other : float
    Home_owner : float
    Home_parents : float
    Home_private : float
    Home_rent : float
    Marital_married : float
    Marital_separated : float
    Marital_single : float
    Marital_widow : float
    Records_yes : float
    Job_freelance : float
    Job_others : float
    Job_partime : float


#cargamos el modelo
creditRisk_model = pickle.load(open('creditRisk_model.sav','rb'))

#endpoint
@app.post('/creditRisk_prediction')
def creditRisk_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    #json to dictionary
    input_dictionary = json.loads(input_data)

    seniority = input_dictionary['Seniority']
    time = input_dictionary['Time']
    age = input_dictionary['Age']
    expenses = input_dictionary['Expenses']
    income = input_dictionary['Income']
    assets = input_dictionary['Assets']
    debt = input_dictionary['Debt']
    amount = input_dictionary['Amount']
    price = input_dictionary['Price']
    home_other = input_dictionary['Home_other']
    home_owner = input_dictionary['Home_owner']
    home_parents = input_dictionary['Home_parents']
    home_private = input_dictionary['Home_private']
    home_rent = input_dictionary['Home_rent']
    marital_married = input_dictionary['Marital_married']
    marital_separated = input_dictionary['Marital_separated']
    marital_single = input_dictionary['Marital_single']
    marital_widow = input_dictionary['Marital_widow']
    records_yes = input_dictionary['Records_yes']
    job_freelance = input_dictionary['Job_freelance']
    job_others = input_dictionary['Job_others']
    job_partime = input_dictionary['Job_partime']

    input_list = [seniority,time, age,expenses, income, assets, debt, amount, price, home_other, home_owner, home_parents, home_private, home_rent, marital_married, marital_separated, marital_single, marital_widow, records_yes, job_freelance, job_others, job_partime]

    prediction = creditRisk_model.predict([input_list])

    if prediction[0] == 0:
        return 'ok'
    else:
        return 'default'