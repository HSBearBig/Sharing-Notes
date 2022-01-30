from django.db import models

# Create your models here.

class NoteUpload(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    desc = models.TextField()
    upload_time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='upload_images/')
    def __str__(self):
        return self.author + self.upload_time.strftime("%m/%d/%Y, %H:%M:%S")

class Academy(models.Model):
    academy = models.CharField(max_length=20)
    def __str__(self):
        return self.academy

class Department(models.Model):
    academy = models.ForeignKey("Academy", on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    def __str__(self):
        return self.department

class Subject(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    def __str__(self):
        return self.subject