import json
from urllib import response
import requests

url = 'http://127.0.0.1:8000/creditRisk_prediction'

input_data_for_model = {

    'Seniority': 0.1,
    'Time' : 0.2,
    'Age' : 0.3,
    'Expenses' : 0.4,
    'Income' : 0.5,
    'Assets' : 0.6,
    'Debt' : 0.01,
    'Amount' : 0.02,
    'Price' : 0.1,
    'Home_other' : 0.1,
    'Home_owner' : 0.3,
    'Home_parents' : 0.02,
    'Home_private' : 0.1,
    'Home_rent' : 0.01,
    'Marital_married' : 0.01,
    'Marital_separated' : 0.1,
    'Marital_single' : 0.1,
    'Marital_widow' : 0.01,
    'Records_yes' : 0.02,
    'Job_freelance' : 0.1,
    'Job_others' : 0.2,
    'Job_partime' : 0.8
}

input_json = json.dumps(input_data_for_model)
reponse = requests.post(url, data=input_json)

print(response.text)