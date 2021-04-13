from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Subdivision(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL,
                                    blank=True, null=True, related_name='directors',
                                    verbose_name=_('Начальник'))

    class Meta:
        verbose_name = _('Подразделение')
        verbose_name_plural = _('Подразделения')

    def __str__(self):
        return self.name


class Position(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')

    def __str__(self):
        return self.name


class Employee(models.Model):
    fio = models.CharField(max_length=255, verbose_name=_('ФИО'))
    date_of_birth = models.DateField(verbose_name=_('Дата рождения'))
    photo = models.ImageField(upload_to='employee/photo', verbose_name=_('Фото'))
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='staff', verbose_name=_('Подразделение'))
    position = models.ForeignKey(Position, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='staff', verbose_name=_('Должность'))

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

    def __str__(self):
        return self.fio
