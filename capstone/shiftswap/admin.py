from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User, JobCard
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'is_contractor', 'is_employer', 'company', 'company_location']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_contractor', 'is_employer', 'company', 'company_location')}),
    ) #this will allow to change these fields in admin module

admin.site.register(User, UserAdmin)
admin.site.register(JobCard)
