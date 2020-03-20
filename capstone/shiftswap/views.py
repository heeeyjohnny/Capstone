from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, JobCard
import json


# Create your views here.
def index(request):
    data = JobCard.objects.order_by('date')
    # opening json data file
    ## loaded a mock json with data info, parsed and then save to database
    # with open('capstone/shiftswap/MOCK_DATA.json') as f:
    #     data = json.load(f)
    # for x in data:
    #     company = x['company']
    #     type = x['type']
    #     date = x['date']
    #     start_time = x['start_time']
    #     end_time = x['end_time']
    #     pay = x['pay']
    #     logo = x['logo']
    #     post = JobCard(employer=User(id=3,company=company), type=type, date=date, start_time=start_time, end_time=end_time, pay=pay, description=logo)
    #     post.save()
    context = {
    'data': data,
    }
    return render(request, 'shiftswap/index.html', context)

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    is_employer = request.POST['inlineRadioOptions']
    is_contractor = request.POST['inlineRadioOptions']
    if request.POST['inlineRadioOptions'] == 'is_employer':
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=True, is_employer=True) #is_employer or is_contractor=True
        user.save()
    else:
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=True, is_contractor=True)
        user.save()

    # User.objects.create_user(username, email, password)
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
    # print(request.POST)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('shiftswap:index'))
    else:
        return HttpResponseRedirect(reverse('shiftswap:login_user'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('shiftswap:index'))

@login_required
def post(request):
    if request.user.is_employer or request.user.is_superuser:
        current_user = request.user
        context = {
        }
        return render(request, 'shiftswap/post.html', context)
    else:
        return HttpResponseRedirect(reverse('shiftswap:index'))

@login_required
def apply(request):
    if request.user.is_authenticated:
        return HttpResponse('Apply page/Job info page')
    else:
        return HttpResponseRedirect(reverse('shiftswap:login_user'))

@login_required
def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        # print('>>>>>>>>>>>>>')
        # print(current_user.__dict__)
        # print(current_user.username)
        # print(current_user.email)
        # print(current_user.id)
        context = {
        }
        return render(request, 'shiftswap/profile.html', context)
    else:
        return HttpResponseRedirect(reverse('shiftswap:index'))
