from django.db import models
from datetime import date
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.TextField()

    def __str__(self):
        return self.name
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name
#clients
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)  # ← this makes it optional



    def __str__(self):
        return self.name

class DrillingRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    request_date = models.DateField(default=date.today)  # ✅ Correct way
    location = models.CharField(max_length=100)
    depth_required = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Request by {self.client.name} - {self.status}"


class ProjectProgress(models.Model):
    request = models.ForeignKey(DrillingRequest, on_delete=models.CASCADE)
    date = models.DateField()
    progress_note = models.TextField()

    def __str__(self):
        return f"{self.request} - {self.date}"

#new codes

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description')  # ← this fixes it
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.IntegerField(default=0)  # e.g. 0 to 100
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name