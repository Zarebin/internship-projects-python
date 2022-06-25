from locust import HttpUser,task,constant
from json import loads
from random import choice

BASE_URL = 'http://127.0.0.1:8000/'

post_cookie_user_1 = {'csrftoken':''}
 
responses = ('top','bottom','similar', 'skip') 
questions = ("1","2","3")
users = ("1")

class FoodCompareTest(HttpUser):

    host:BASE_URL                        
    wait_time =constant(1)   
    
    @task(1)
    def get_data(self):

        res_get = self.client.get(url='food_compare/test/') 
        print('status: ',res_get.status_code)
        print(loads(res_get.text))
        
        
    @task(1)
    def post_data(self):

        res_post = self.client.post(url='test/food_compare/',
        data= {
            "response":choice(responses),
            "question":choice(questions), 
            "user" :choice(users)            },
        cookies=post_cookie_user_1)

        print('status: ',res_post.status_code)  
        print(loads(res_post.text))
         











