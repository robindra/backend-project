from django.conf import settings
from django.db import models

# Create your models here.

class StateChoices(models.IntegerChoices):
    NOT_YET = 0, 'Not Yet'
    STARTED = 1, 'Started'
    PAUSED = 2, 'Paused'
    COMPLETED = 3, 'Completed'

class DeviceChoices(models.IntegerChoices):
    MOBILE = 1, 'Mobile'
    TABLET = 2, 'Tablet'
    LAPTOP = 3, 'Laptop'
    COMPUTER = 4, 'Computer'


class Projects(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects_updated', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    total_survey = models.IntegerField()
    state = models.CharField(max_length=10, choices=StateChoices.choices)
    allow_devices = models.CharField(max_length=50, choices=DeviceChoices.choices)
    allow_countries = models.JSONField()  # Storing country names as a list

    def __str__(self) -> str:
        return self.name

class ProjectStatus(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    started = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)
    in_progress = models.IntegerField(default=0)
    drop_off = models.IntegerField(default=0)
    screen_out = models.IntegerField(default=0)
    rotten = models.IntegerField(default=0)
    disqualified = models.IntegerField(default=0)

    def __str__(self):
        return f"Status of {self.project.name}"

class SurveyProgressStatus(models.IntegerChoices):
    DISQUALIFIED = 0, 'Disqualified' 
    STARTED = 1, 'Started'
    COMPLETED = 2, 'Completed'
    IN_PROGRESS = 3, 'In Progress'
    DROP_OFF = 4, 'Drop Off'
    SCREEN_OUT = 5, 'Screen Out'
    ROTTEN = 6, 'Rotten'


class UserSurveyStatus(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_unique_identification = models.CharField(max_length=100) 
    current_status = models.CharField(max_length=20, choices=SurveyProgressStatus.choices)

    def __str__(self):
        return f"User {self.user} status for {self.project.name}"