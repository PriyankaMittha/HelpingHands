from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=300,null=True)
    userpic=models.FileField(null=True)
    regdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=300,null=True)
    userpic=models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme=models.CharField(max_length=300,null=True)
    status=models.CharField(max_length=20,null=True)
    regdate=models.DateTimeField(auto_now_add=True)
    adminremark=models.CharField(max_length=300,null=True)
    updationdate=models.DateField(null=True)
    def __str__(self):
        return self.user.username

class Organization(models.Model):
    areaname=models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100, null=True)
    description=models.CharField(max_length=300,null=True)
    creationdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.areaname

class Donation(models.Model):
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100,null=True,blank=True)
    donationpic = models.FileField(null=True,blank=True)
    collectionloc = models.CharField(max_length=300,null=True,blank=True)
    description = models.CharField(max_length=300,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    donationdate = models.DateTimeField(auto_now_add=True,blank=True)
    adminremark = models.CharField(max_length=300,null=True,blank=True)
    volunteer = models.ForeignKey(Volunteer,on_delete=models.CASCADE, blank=True, null=True)
    donationarea = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    volunteerremark = models.CharField(max_length=300,null=True,blank=True)
    updationdate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.donationname

class Gallery(models.Model):
    donation=models.ForeignKey(Donation,on_delete=models.CASCADE)
    deliverypic=models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donation.donationname

class PaymentDetails(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    donationarea = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)


















    