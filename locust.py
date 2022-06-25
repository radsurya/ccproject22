import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(1, 5)

  @task
  def movie_service(self):
    self.client.get(url="/fc44311/ccproject22/1.0.0/ui/")

  @task
  def movie_service_get_by_id(self):
    self.client.get(url="/fc44311/ccproject22/1.0.0/movie/get_by_id/1066")
