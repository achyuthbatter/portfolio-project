from django.shortcuts import render, get_object_or_404

from .models import Job, JobDetail

# Create your views here.

def home(request):
    jobs = Job.objects.all().order_by('-date')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    jobs = get_object_or_404(Job, pk=job_id)
    jobdetail = get_object_or_404(JobDetail, job_id=job_id)
    return render(request, 'jobs/jobdetail.html', {'jobdetail': jobdetail, 'jobs': jobs})