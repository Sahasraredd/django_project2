from django.shortcuts import render
from jobs.models import job

# Create your views here.
def Active_job(request):
    job_list = job.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'jobs/index.html',context=my_dict)