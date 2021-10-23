from django.db import models
from django.contrib.auth.models import User
from help.models import RequestForHelp


class Role(models.Model):
    """ Модель для указания ролей (стажер/эксперт) """
    nameRole = models.CharField(verbose_name="Название роли",
                                max_length=20)

    def __str__(self):
        return str(self.nameRole)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Skill(models.Model):
    """ Модель навыков """
    nameSkill = models.CharField(verbose_name='Название навыка',
                                 max_length=100,
                                 )
    descriptionSkill = models.TextField(verbose_name="Описание навыка",
                                        blank=True,
                                        null=True
                                        )

    def __str__(self):
        return str(self.nameSkill)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Portfolio(models.Model):
    """ Модель портфолио """
    internPortfolio = models.OneToOneField(User,
                                           on_delete=models.CASCADE,
                                           verbose_name='Имя стажера',
                                           )
    descriptionPortfolio = models.TextField(verbose_name="Описание портфолио")
    achievementsPortfolio = models.TextField(verbose_name="Достижение")
    participationInProjectPortfolio = models.TextField(verbose_name="Участие в проектах")

    def __str__(self):
        return str(self.internPortfolio)

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class improvedUserModel(models.Model):
    """ Кастомная модель пользователя """
    name = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='Имя стажера',
                                )
    role = models.OneToOneField(Role,
                                on_delete=models.CASCADE,
                                verbose_name='Роль',
                                )
    skills = models.ManyToManyField(Skill,
                                    verbose_name='Навыки стажера',
                                    blank=True,
                                    )
    portfolio = models.OneToOneField(Portfolio,
                                     on_delete=models.CASCADE,
                                     verbose_name='Портфолио стажера',
                                     )
    rating = models.IntegerField(verbose_name="Рейтинг",
                                 default=0
                                 )

    requestToExpert = models.ManyToManyField(RequestForHelp,
                                             verbose_name='Запросы',
                                             blank=True,
                                             )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
