from django.db import models
# from mysite.app.forms import ContactForm

# Create your models here.

class FormData(models.Model):
    RegistrationId = models.AutoField(primary_key=True)
    email = models.EmailField("Email Id", max_length=30)
    name = models.CharField("Name", max_length=50)
    dob = models.DateField("Date of Birth")
    #LastName = models.CharField("Last Name", max_length=50)
    Password = models.CharField("Password", max_length=20)
    confpass = models.CharField("Confirm Password",max_length=20)
    MobileNo = models.CharField("Mobile Number", max_length=15)
    
    #genderchoice=[('Male','Male'),('Female','Female')]
    gender = models.CharField("Gender",max_length = 10)
    
    #countrychoice=[('1','India'),('2','USA'),('3','UK')]
    country = models.CharField("country",max_length = 20)
    #country = models.ChoiceField()
    def __unicode__(self):
        return u'%s %s' % (self.name, self.country)
    

