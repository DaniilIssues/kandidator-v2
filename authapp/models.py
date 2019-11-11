from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    telephone_num = models.CharField(max_length=50)
