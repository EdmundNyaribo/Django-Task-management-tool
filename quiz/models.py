from django.db import models

# Create your models here.
class schedule(models.Model):
    Task = models.CharField(max_length=40, blank=False, null=False)
    Description = models.CharField(max_length=200, blank=False, null=False)
    Priority = models.CharField(max_length=6, blank=False, null=False)
    DueDate = models.CharField(max_length=10, blank=False, null=False)
    Status = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.Task