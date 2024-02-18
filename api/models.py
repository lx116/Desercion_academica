from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Basic Data
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    full_name = models.CharField(max_length=240)
    gender = models.CharField(max_length=30)
    nationality = models.CharField(max_length=120)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    personal_id = models.CharField(max_length=16)

    # Contact Data
    personal_mail = models.CharField(max_length=320)
    address = models.CharField(max_length=400)

    # Employ Data
    employment_status = models.BooleanField(default=False)
    employer_info = models.TextField(blank=True, null=True)

    # Academic Data
    university_name = models.OneToOneField('api.University', on_delete=models.CASCADE)
    major = models.CharField()
    academic_level = models.IntegerField()

    def __str__(self):
        return self.user.username


class PersonalityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class University(models.Model):
    # Basic Data
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=20, unique=True)
    founded_date = models.DateField()
    website = models.URLField()
    logo = models.ImageField(upload_to='university_images/', blank=True, null=True)

    # Location Data
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Questions(models.Model):
    number = models.IntegerField()
    info = models.CharField(max_length=500)
    category = models.ForeignKey('api.Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=120)


class Answers(models.Model):
    info = models.CharField(max_length=500)
    char = models.CharField(max_length=1)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)


class UserAnswers(models.Model):
    pass


class PsychologicalTests(models.Model):
    pass
