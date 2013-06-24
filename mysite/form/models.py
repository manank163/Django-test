from django.db import models

# Create your models here.
#from mysite.form.forms import Register

# Create your models here.

class regit(models.Model):
    RegistrationId = models.AutoField(primary_key = True)
    EmailId = models.EmailField("Email Id", max_length=30)
    FirstName = models.CharField("Name", max_length=50)
    dob = models.DateField("date of birth" )
    Password = models.CharField("Password", max_length=25)
    MobileNo = models.CharField("Mobile Number", max_length=15)
    gender = models.CharField("Gender",max_length = 10)
    country = models.CharField("country",max_length = 20)
    
    #country = models.ChoiceField()