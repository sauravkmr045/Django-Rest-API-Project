from django.db import models


class Employee(models.Model):
	ename = models.CharField(max_length =250)
	eno = models.IntegerField()
	esal = models.IntegerField()
	eaddr = models.CharField(max_length=250)
	