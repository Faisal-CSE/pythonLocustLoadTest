from Locust import HttpUser, constant, task

class MyReqRes (HttpUser):
    host = "https://regres.in'
    wait_time = constant(1)
    
    
    @task
    def get users(self):
        res = self.client.get("/api/users?page2")
        print(res.text)
        print(res.status_code)
        print(res.headers)
        
        
    @task
    def create_user (self):
        res = self.client.post("/api/users", data='
        {"name":"morpheus", "job":"Leader"}
        print(res.text)
        print(res.status_code)
        print(res.headers)
