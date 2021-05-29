from django.contrib import admin

# Register your models here.
from .models import Project, Step,Task

admin.site.register(Project)
admin.site.register(Step)
admin.site.register(Task)
