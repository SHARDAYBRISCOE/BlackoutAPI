from rest_framework import serializers
from . models import Employee
from . models import Business

class employeeSerializer(serializers.ModelSerializer):
	class Meta: 
		model=Employee
		fields=('firstname', 'lastname')
		# you can also use fields=__all__ to return all fields for Employee


class businessSerializer(serializers.ModelSerializer):
	class Meta:
		model=Business
		fields=('business_name','website')