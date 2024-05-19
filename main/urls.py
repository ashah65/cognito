from django.urls import path, include
from . import views

urlpatterns = [
  path("requestAJob", views.request_a_job, name='request_job'),
]

