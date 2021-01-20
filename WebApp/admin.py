from django.contrib import admin
from . models import Employee
from . models import Business
# Register your models here.

admin.site.register(Employee)
# convert this model to kson
admin.site.register(Business)
