from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.FloatField()
    hypertension = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    ever_married = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])
    residence_type = models.IntegerField(choices=[(0, 'Rural'), (1, 'Urban')])
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    work_type = models.CharField(max_length=20, choices=[
        ('Govt_job', 'Government Job'), ('Never_worked', 'Never Worked'),
        ('Private', 'Private'), ('Self-employed', 'Self-employed'), ('children', 'Children')
    ])
    smoking_status = models.CharField(max_length=20, choices=[
        ('Unknown', 'Unknown'), ('formerly smoked', 'Formerly Smoked'),
        ('never smoked', 'Never Smoked'), ('smokes', 'Smokes')
    ])
    stroke = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True, blank=True)
    still_working = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # e.g., "Logged in", "Made prediction"
    timestamp = models.DateTimeField(default=timezone.now)
    details = models.TextField(blank=True)  # JSON or text of activity details

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"