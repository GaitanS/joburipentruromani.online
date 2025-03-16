from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
