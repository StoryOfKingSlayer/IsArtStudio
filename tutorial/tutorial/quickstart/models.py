from django.db import models

# Create your models here.
class Project(models.Model):
    projectName = models.CharField("Название", max_length=150)

    def __str__(self):
        return self.projectName

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проект"


class Step(models.Model):
    stepNumber = models.CharField("Номер", max_length=100)
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return  self.stepNumber

    class Meta:
        verbose_name = "Шаг"
        verbose_name_plural = "Шаги"

class User(models.Model):
    FIO = models.CharField("ФИО", max_length=200)
    birthday = models.DateField("Дата рождения")

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "ФИО"

class Task(models.Model):
    taskName = models.CharField("Задача", max_length=100)
    taskStatus = models.BooleanField(default=False)
    step = models.ForeignKey(Step, verbose_name="Шаг", on_delete= models.SET_NULL, null=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.step

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"