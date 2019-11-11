from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from authapp.models import MyUser


class Account(models.Model):
    in_work = 'ON'
    archive = 'AR'
    stopped = 'ST'
    STATUS_CHOICES = {
        (in_work, 'В работе'),
        (archive, 'В архиве'),
        (stopped, 'Приостановлена'),

    }
    name_vacancy = models.CharField(max_length=150)
    created = models.DateTimeField(null=True)
    login_hh = models.CharField(max_length=150)
    password_hh = models.CharField(max_length=150)
    url_selected_hh = models.URLField(max_length=250)
    id_vacancy_hh = models.CharField(max_length=50)
    short_url_hh = models.URLField(max_length=250)
    text_to_sms = models.CharField(max_length=250)
    text_to_email = models.CharField(max_length=350)
    user = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=120, default=in_work)
    move = models.BooleanField(default=True)
    progress = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)

