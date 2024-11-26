from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def busybeesrecipes(self):
        self.client.get("/")
