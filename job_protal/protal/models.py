from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
    

JOB_TYPE_FULL_TIME = "full_time"
JOB_TYPE_PART_TIME = "part_time"
JOB_TYPE_CONTRACT = "contract"
JOB_TYPE_FREELANCE = "freelance"

JOB_TYPE_CHOICES = [
    (JOB_TYPE_FULL_TIME, "Full Time"),
    (JOB_TYPE_PART_TIME, "Part Time"),
    (JOB_TYPE_CONTRACT, "Contract"),
    (JOB_TYPE_FREELANCE, "Freelance"),
]

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    job_category = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, default=JOB_TYPE_FULL_TIME, choices=JOB_TYPE_CHOICES)
    job_experience = models.PositiveIntegerField()
    job_vancancy = models.PositiveIntegerField()
    job_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")

