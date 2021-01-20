from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from .models import Business
from . serializers import employeeSerializer
from . serializers import businessSerializer
from django.http import JsonResponse
#class employeeList(APIView):
#	def get(self, request):
#		employees1=Employee.objects.all()
#		serializer=employeeSerializer(employees1, many=True)
#		return Response(serializer.data)
		#reading or taking data

#	def post(self):
#		pass

#class businessList(APIView):
#	def get(self, request):
#		business1=Business.objects.all()
#		serializer=businessSerializer(business1, many=True)
#		return Response(serializer.data)

#	def post(self):
#		pass


def test_view(request):
	data = {
	'name':'john',
	'age': 23
	}
	return JsonResponse(data)
