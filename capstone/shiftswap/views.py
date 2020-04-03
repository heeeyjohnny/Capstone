from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User, JobCard
from datetime import date, datetime, timedelta
import json


def index(request):
    data = JobCard.objects.order_by('-date')
    user = User.objects.all()
    job_list = JobCard.objects.get_queryset().order_by('-date')
    page = request.GET.get('page', 1)

    paginator = Paginator(job_list, 8)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    # opening json data file
    ## loaded a mock json with data info, parsed and then save to database
    # with open('/Users/johnnyphompadith/Desktop/CODE/Capstone/capstone/shiftswap/MOCK_DATA.json') as f:
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
    'user': user,
    'jobs': jobs,
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
    login(request, user)
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

def postjob(request):
    print(request.POST)
    jobs = JobCard.objects.all()
    type = request.POST['type']
    pay = request.POST['pay']
    date = request.POST['date']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    postingjob = JobCard.objects.create(type=type, employer=request.user, pay=pay, date=date, start_time=start_time, end_time=end_time)
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
def applyjob(request, id):
    if request.method == 'GET':
        user = request.user.id
        job = JobCard.objects.get(id=id)
        job.applied.add(request.user)
        # in jobinfo page, when click apply, sends request through applyjob views with jobid, if request.method is get, pull id out
        # testing prints
        # print('>>>>')
        # print(job.id)
        # print(request.user.id)
    return HttpResponseRedirect(reverse('shiftswap:index'))

@login_required
def apply(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            job = JobCard.objects.get(id=id)
            user = User.objects.all()
            now = datetime.now()
            dt = datetime.combine(job.date, datetime.min.time())
            job_posted_date = dt - now
            context = {
            'job': job,
            'job_posted_date': job_posted_date,
            'user': user,
            }
        return render(request, 'shiftswap/jobinfo.html', context)
    else:
        return HttpResponseRedirect(reverse('shiftswap:login_user'))

@login_required
def edit(request, id):
    if request.user.is_authenticated:
        editjob = JobCard.objects.get(id=id)
        context = {
        'editjob': editjob,
        }
        return render(request, 'shiftswap/edit.html', context)
    else:
        return HttpResponseRedirect(reverse('shiftswap:login_user'))


@login_required
def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        # searches for all jobs applied for by requested user.
        postedjobs = JobCard.objects.filter(employer=request.user)
        lookingup = JobCard.objects.filter(applied=request.user)
        # print('>>>>>>>>>>>>>')
        # print(current_user.__dict__)
        # print(current_user.username)
        # print(current_user.email)
        # print(current_user.id)
        context = {
        'postedjobs': postedjobs,
        'lookingup': lookingup,
        }
        return render(request, 'shiftswap/profile.html', context)
    else:
        return HttpResponseRedirect(reverse('shiftswap:index'))
