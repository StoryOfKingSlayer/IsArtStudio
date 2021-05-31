from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    projectName = models.CharField("Название", max_length=150)
    description = models.CharField("Опсианеи", max_length=150, default='SOME STRING')

    def __str__(self):
        return f'{self.id}_{self.projectName}'

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Task(models.Model):
    taskName = models.CharField("Задача", max_length=100)
    taskStatus = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class CheckList(models.Model):
    stepNumber = models.CharField("Номер", max_length=100)
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}_{self.stepNumber}'

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"
