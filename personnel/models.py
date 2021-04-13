from django.db import models
from django.utils.translation import gettext_lazy as _


class Subdivision(models.Model):
    pass

    class Meta:
        verbose_name = _('Подразделение')
        verbose_name_plural = _('Подразделения')


class Position(models.Model):
    pass

    class Meta:
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')


class Employee(models.Model):
    pass

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')
