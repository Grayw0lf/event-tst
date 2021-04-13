from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Subdivision, Position, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['fio', 'date_of_birth', 'photo', 'subdivision', 'position']


@admin.register(Subdivision)
class SubdivisionAdmin(MPTTModelAdmin):
    fields = ['name', 'parent', 'director']


@admin.register(Position)
class PositionAdmin(MPTTModelAdmin):
    fields = ['name', 'parent']
