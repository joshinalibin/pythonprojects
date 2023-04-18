from django.db import models
from django.db.models import CASCADE


# Create your models here.
class District(models.Model):
    districtname = models.CharField(max_length=100)

    def __str__(self):
        return self.districtname


class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=CASCADE)
    branchname = models.CharField(max_length=100)

    def __str__(self):
        return self.branchname


class Details(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    ACCOUNT_TYPES = (
        ('A', 'select Account'),
        ('S', 'Savings'),
        ('C', 'Current'),
        ('L', 'Loan'),
        ('F', 'Fixed'),
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    materials_required = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


