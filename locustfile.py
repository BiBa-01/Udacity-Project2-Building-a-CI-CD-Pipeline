from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test1(self):
        self.client.get("http://localhost:5000")

    @task(2)
    def test2(self):
        self.client.post("http://localhost:5000/predict")
     
if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

#class WebsiteUser(HttpLocust):
 #  task_set = UserBehavior
       
