from django.shortcuts import render
import random
from .models import Job

# Create your views here.

def request_a_job(request):
  if request.method == 'POST':
    email = request.POST['email']
    title = request.POST['title']
    description = request.POST['desc']
    pay = request.POST['pay']
    date = request.POST['dates']
    i = random.randint(0, 100000)
    j = Job(i, email, title, description, pay, date)
    j.save()
  return render(request, 'authentication/requestAJob.html')

