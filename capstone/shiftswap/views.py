from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, JobCard
import json


# Create your views here.
def index(request):
    # opening json data file
    with open('/Users/johnnyphompadith/Desktop/CODE/Capstone/capstone/shiftswap/MOCK_DATA.json') as f:
        data = json.load(f)
    # print(data)
    jobs = JobCard.objects.all()
    context = {
    'jobs': jobs,
    'data': data,
    }
    return render(request, 'shiftswap/index.html', context)

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # User.objects.create_user(username, email, password)
    print(request.POST)
    # register = User.objects.create_user(username=username, email=email, password=password) #is_employer or is_contractor=True
    print(register)
    return HttpResponseRedirect(reverse('shiftswap:index'))
