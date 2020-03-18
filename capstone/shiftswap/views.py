from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


def info(request):
    jobs = JobCard.objects.all()
    context = {
    'jobs': jobs,
    }
    return render(request, 'shiftswap/jobinfo.html', context)

def login_user(request):
    if request.method == 'GET':
        return render(request, 'shiftswap/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(request.POST)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('shiftswap:index'))
    else:
        return HttpResponse('error')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('shiftswap:index'))

@login_required
def post(request):
    if request.user.is_employer or request.user.is_superuser:
        return HttpResponse('ok')
    else:
        return HttpResponse('No')

@login_required
def apply(request):
    if request.user.is_authenticated:
        return HttpResponse('ok')
    else:
        return HttpResponseRedirect(reverse('shiftswap:login_user'))
