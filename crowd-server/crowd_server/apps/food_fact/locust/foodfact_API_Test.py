from locust import HttpUser,task,constant
#from locust import user,between,SequentialTaskSet
from json import loads
from random import choice

BASE_URL='http://127.0.0.1:8000/question/'

users = ("1","2")
responses = ("0","1","2","3")
questions = ("1","2","3")


class FoodFactTest(HttpUser):
    host:BASE_URL                        
    wait_time =constant(1)   # wait_time =between(0.5,1)
    # weight = 3 between class  |   use  -> task(3) task(2) between tasks
    # fixed_count = 1

    @task(2)
    def get_data(self):

        res_get = self.client.get(url='question/') 
        print('status: ',res_get.status_code)
        print(loads(res_get.text))
        
    @task(1)
    def post_data(self):

        res_post = self.client.post(url='question/',
        data= {
            "user" :choice(users),
            "response":choice(responses),
            "question":choice(questions)  })

        print('status: ',res_post.status_code)  
        print(loads(res_post.text))
         











