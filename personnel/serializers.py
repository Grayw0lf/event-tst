from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Employee, Position, Subdivision


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('fio', 'date_of_birth', 'photo', 'subdivision', 'position')


class PositionSerializer(serializers.ModelSerializer):
    parent = RecursiveField(allow_null=True)

    class Meta:
        model = Position
        fields = ('name', 'parent')


class SubdivisionSerializer(serializers.ModelSerializer):
    parent = RecursiveField(allow_null=True)
    director = EmployeeSerializer()

    class Meta:
        model = Subdivision
        fields = ('name', 'parent', 'director')
