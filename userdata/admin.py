from django.contrib import admin
from userdata.models import TrainingData
from userdata.models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'legal_name', 'manager', 'l3', 'l2', 'l1',
    'job_title', 'job_code', 'location', 'region')
    search_fields = ['eeid', 'username', 'legal_name', 'fname', 'lname',
    'manager', 'l1', 'l2', 'l3', 'email', 'hire_date', 'job_code',
    'job_title']

class TrainingDataAdmin(admin.ModelAdmin):
    list_display = ('uname', 'lp_name', 'item_name', 'item_status', 'item_type', 'hire_date', 'due_date')
    search_fields = ['uname__username', 'lp_name', 'item_name', 'item_status', 'item_type', 'hire_date', 'due_date']



admin.site.register(TrainingData, TrainingDataAdmin)
admin.site.register(UserData, UserDataAdmin)