from Blog import app, db
from flask import render_template 
from Blog.models import Psychology_tests, test_results
import urllib.request, json
import requests

@app.route('/')
def home():
    return "Hello"


@app.route('/psychology', methods=['GET', 'POST'])
def psycology_test():

    API_Key = '...'
    Method = 'tests'
    url = 'https://api.psychometrist.ir/v1/%s/%s' %(API_Key, Method)
    resp_1 = requests.get(url)

    Method = 'questionAnswers'
    url = 'https://api.psychometrist.ir/v1/%s/%s' %(API_Key, Method)
    resp_2 = requests.get(url)

    tests = Psychology_tests(id= resp_1.json()['id'], title= resp_1.json()[''], 
                             description=resp_2.json()['description'], question_count=resp_1.json()['questions_count'],)
    

@app.result('/results', methods=['GET','POST'])
def results():
    API_Key = '...'
    Method = 'result'
    url = 'https://api.psychometrist.ir/v1/%s/%s' %(API_Key, Method)
    resp = requests.get(url)

    ans = test_results(id=ans.json()['id'] )






