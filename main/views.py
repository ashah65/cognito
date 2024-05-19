from django.shortcuts import render
from .models import Job

# Create your views here.

def request_a_job(request):
  if request.method == 'POST':
    title = request.post['title']
    description = request.post['desc']
    pay = request.post['pay']
    date = request.post['dates']
    j = Job(title, description, pay, date)
    j.save()
  return render(request, 'authentication/requestAJob.html')

