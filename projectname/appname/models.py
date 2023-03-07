from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.manager.name})"

class Manager(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"
