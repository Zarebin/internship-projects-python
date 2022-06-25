from locust import HttpUser,task,constant
from json import loads
from random import choice

BASE_URL='http://127.0.0.1:8000/'

users = ('1','2','3')
images = ( '1','2','3')
answers = ('0','1','2','3')


ctrftoken = ''
post_cookies = {'csrftoken':f'{ctrftoken}'}
post_head = {'Cookie': f'csrftoken={ctrftoken}',
        'X_CSRFToken':f'{ctrftoken}'}

class ImageLabelTest(HttpUser):
    
    host:BASE_URL                        
    wait_time =constant(1)   
    
    @task()
    def get_ImageCategory(self):

        res_get = self.client.get(url='image-label/categories/') 
        print('status: ',res_get.status_code)
        print(loads(res_get.text))
        
    @task()
    def get_ImageViewAPI(self):

        res_post = self.client.get(url='image-label/image/')

        print('status: ',res_post.status_code)  
        print(loads(res_post.text))


    @task()
    def post_ImageViewAPI(self):

        res_post = self.client.post(url='image-label/image/',
        data= {
            "users" :choice(users),
            "images":choice(images),
            "answers":choice(answers)  })

        print('status: ',res_post.status_code)  
        print(loads(res_post.text))


        
         











