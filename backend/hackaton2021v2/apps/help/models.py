from django.db import models
from django.contrib.auth.models import User


class RequestForHelp(models.Model):
    """ Модель запроса на помощь стажеру """
    nameIntern = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   verbose_name='Имя стажера',
                                   blank=True,
                                   null=True
                                   )
    titleRequest = models.CharField(verbose_name="Тема запроса",
                                    max_length=150,
                                    blank=True,
                                    null=True
                                    )
    textRequest = models.TextField(verbose_name="Текст запроса",
                                   blank=True,
                                   null=True
                                   )
    requiredSkill = models.CharField(verbose_name="Требуемый навык",
                                     max_length=100,
                                     blank=True,
                                     null=True
                                     )

    def __str__(self):
        return str(self.titleRequest)

    class Meta:
        verbose_name = 'Запрос на помощь'
        verbose_name_plural = 'Запросы на помощь'
