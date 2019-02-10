from django.db import models
from classes.models import Classroom
from rest_framework import serializers

class ApiListViewClass(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','year','teacher']

class ApiDetailViewClass(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class ApiUpdateViewClass(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class ApiCreateViewClass(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher']


