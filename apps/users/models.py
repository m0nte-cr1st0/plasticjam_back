from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'

GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female')
)

class User(AbstractUser):
    """
    Extend Django User model
    """
    username = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=GENDER_MALE)
    ip_address = models.GenericIPAddressField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Statistic(models.Model):
    """
    User statistics
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='statistics')
    date = models.DateField(db_index=True)
    page_views = models.PositiveSmallIntegerField()
    clicks = models.PositiveSmallIntegerField()
