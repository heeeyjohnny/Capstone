from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'shiftswap'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('register/', views.register, name='register'),
  path('post/', views.post, name='post'),
  path('login_user/', views.login_user, name='login_user'),
  path('apply/', views.apply, name='apply'),
  path('apply/<int:id>', views.apply, name='apply'),
  path('info/', views.info, name='info'),
  path('logout_user/', views.logout_user, name='logout'),
  path('profile/', views.profile, name='profile'),
]
