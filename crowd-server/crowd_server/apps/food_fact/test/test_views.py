import pytest
import json
from django.contrib.auth import get_user_model

URL = 'http://127.0.0.1:8000/food_fact/question/'


#    The answers we expect to be correct 
@pytest.mark.django_db            
def test_post(client,django_db_setup):

     post_msg =  { 
          "user" : "1",
          "response" : "1",
          "question" : "1"}
     response = client.post(URL, data=post_msg) 
     assert json.loads(response.content ) == {'data': {'id': 1, 'question': 1, 'response': '1', 'user': 1}},'DATA Error'
     assert response.status_code == 201  ,'status Error'     
  

@pytest.mark.django_db               
def test_get(client,django_db_setup):

     get_msg = {'data':[{
          'img_url':'/A.jpg',
          'language':'fa',
          'question':'what you see in this picture?',
          'response_count': 1}]}
     response = client.get(URL) #user_data
     assert json.loads(response.content ) == get_msg ,'data Error'
     assert response.status_code == 202  ,'status Error'       #  json.loads(response.content ) == {"data":[]}
  

#    The answers we expect to be wrong
EXAMPLE_MSG = {'data':[{
     'img_url':'/A.jpg',
     'language':'fa',
     'question':'what you see in this picture?',
     'response_count': 1}]}
EXAMPLE_MSG2 = {'data':[{
     
      'language':'fa',
     'question':'what you see in this picture?',
     'response_count': 1}]}     

@pytest.mark.django_db
@pytest.mark.parametrize(
     'response,status_code',[
          (EXAMPLE_MSG, None),
          ( None, 400),
          (EXAMPLE_MSG2, 500),
          (EXAMPLE_MSG2, 202)
])
def test_data_validation_get( response,status_code, client,django_db_setup):

     response = client.get(URL)
     assert response.status_code != status_code ,"status Error -> status should be 202"
     assert json.loads(response.content ) != response , "data Error -> data should be EXAMPLE_MSG "
   

@pytest.mark.django_db
@pytest.mark.parametrize(
     'data,response,status_code',[
          (None, None, 400),
          (None, EXAMPLE_MSG, 400),
          (EXAMPLE_MSG, None, 201),
          (EXAMPLE_MSG2, {'data': {'id': 1, 'question': 1, 'response': '1', 'user': 1}}, 201)
          
])
def test_data_validation_post( data,status_code,response, client,django_db_setup):

     response = client.post(URL,data=data)
     assert response.status_code != status_code ,"status Error -> status should be 202"
     assert json.loads(response.content ) != response ,"response Error -> data should be {'data':{'id':, 'question':, 'response':, 'user':}}) "
   
     


