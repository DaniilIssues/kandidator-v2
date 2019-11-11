from django.db import models
from django.utils.timezone import now

from authapp.models import MyUser


class Account(models.Model):
    in_work = 'ON'
    archive = 'AR'
    stoped = 'ST'
    STATUS_CHOICES = {
        (in_work, 'В работе'),
        (archive, 'В архиве'),
        (stoped, 'Приостановлена'),

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


class BidModel(models.Model):
    ON_LOAD = 'ol'
    IN_WORK = 'iw'
    STOPED = 'st'
    THE_END = 'en'
    STATUS_CHOICES = [
        (ON_LOAD, 'В обработке'),
        (IN_WORK, 'В работе'),
        (STOPED, 'Остановлен'),
        (THE_END, 'Завершен'),
    ]
    date_create = models.DateTimeField(default=now)
    id_job = models.IntegerField('ID вакансии')
    short_link = models.URLField('Короткая ссылка на', max_length=100)
    url_selection_of_candidates = models.URLField('URL выборки кандидатов')
    count_of_candidates = models.IntegerField('Количество кандидатов')
    prompt_text_letter = models.TextField('Текст приглашения в письме')
    prompt_text_sms = models.TextField('Текст приглашения в СМС')
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ON_LOAD,
    )
    progress = models.IntegerField('Прогресс выполнения')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    move = models.BooleanField(default=True)

    def verbose_name(self):
        return dict(self.STATUS_CHOICES)[self.status]
