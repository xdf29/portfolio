from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):

    job_list = Job.objects.all()

    return render(request, "jobs/home.html", {"job_list":job_list})