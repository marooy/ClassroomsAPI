from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView ,RetrieveUpdateAPIView ,DestroyAPIView
from classes.models import Classroom
from .serializers import ApiListViewClass ,ApiDetailViewClass ,ApiUpdateViewClass ,ApiCreateViewClass

# Create your views here.

class ApiListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ApiListViewClass

class ApiDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ApiDetailViewClass
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ApiCreateView(CreateAPIView):
	serializer_class = ApiCreateViewClass
	def preform_action(self,serializer):
		serializer.save(teacher = self.request.user)

class ApiUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ApiUpdateViewClass
	lookup_field ='id'
	lookup_url_kwarg = 'classroom_id'

class ApiDeleteView(DestroyAPIView):
	queryset =Classroom.objects.all()
	lookup_field ='id'
	lookup_url_kwarg = 'classroom_id'	



