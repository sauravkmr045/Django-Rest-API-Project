from rest_framework import serializers
from app1.models import	Employee

'''def multiple_of_thousand(value): # user defined Validator
	if value%1000 != 0:
		raise serializers.ValidationError('Salary should be multiple of thousands')'''


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


	'''ename = serializers.CharField(max_length =250)
	eno = serializers.IntegerField()
	esal = serializers.IntegerField()#validators = [multiple_of_thousand,]
	eaddr = serializers.CharField(max_length=250)'''

	'''def validate_esal(self,value): #if we want to validate one field at a time then we use this method
	# We need to prefix the validate before the column name
		if value<5000:
			raise serializers.ValidationError('Employee Salary must be greater than 5000')'''

	'''def validate(self,data): # If we want to validate multiple field validation then we use this approach Validation is a keyword here
		ename = data.get('ename')
		esal = data.get('esal')
		if ename.lower() =='saurav':
			if esal <6000:
				raise	serializers.ValidationError("Saurav's salary shoule be greater than 6000")
		return data
'''

	'''
	def create(self,validated_data):
		return Employee.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.eno = validated_data.get('eno',instance.eno)
		instance.esal = validated_data.get('esal',instance.esal)
		instance.ename = validated_data.get('ename',instance.ename)
		instance.eaddr = validated_data.get('eaddr',instance.eaddr)
		instance.save()
		return instance

		'''