from django.contrib import admin

# Register your models here.
from .models import Project, CheckList, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName', 'description')


class CheckListAdmin(admin.ModelAdmin):
    list_display = ('id', 'stepNumber', 'project', 'user', 'task')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskName', 'taskStatus')


admin.site.register(Project, ProjectAdmin)
admin.site.register(CheckList, CheckListAdmin)
admin.site.register(Task, TaskAdmin)
