import time
from locust import HttpUser, task, between, TaskSet



class webUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_page(self):
        self.client.get("/")

    @task
    def load_predict(self):
        self.client.post("/predict", json={
    "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }        
})    

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        self.client.get("/")

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
