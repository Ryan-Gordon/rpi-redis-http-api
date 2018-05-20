from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task(3)
    def index(l):
        l.client.get("/v1.0/ui")
    @task(2)
    def todays_champion(l):
        l.client.get("/v1.0/todays-champion")
   
    @task(2)
    def get_leaderboard(l):
        l.client.get("/v1.0/today-leaderboard/")
class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 15000