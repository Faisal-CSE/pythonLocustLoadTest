import random
import string

from locust import HttpUser, SequentialTaskSet, constant, task


class SequentialData1(SequentialTaskSet):
    sessionId = ''.join(random.choice(string.ascii_uppercase) for i in range(10))

    @task
    def taskOne(self):
        self.client.get("/200")
        print("From task one ... " + self.sessionId)

    @task
    def taskTwo(self):
        self.client.get("/500")
        print("From task two ... " + self.sessionId)
        self.sessionId = ''.join(random.choice(string.ascii_uppercase) for i in range(10))


class SequentialData2(SequentialTaskSet):

    @task
    def taskThree(self):
        self.client.get("/200")
        print("From task three ...")


class ActionClass(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [SequentialData1]
