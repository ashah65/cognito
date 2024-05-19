from django.urls import path, include
from . import views

urlpatterns = [
  path("request-job", views.request_a_job, name='request_job'),
]

