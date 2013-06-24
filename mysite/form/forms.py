from django import forms
from django.forms import ModelForm
from mysite.form.models import regit

class Register(forms.ModelForm):
	class Meta:
		model = regit
		
	#password = forms.CharField(min_length=7, widget=forms.PasswordInput())
	
	genderchoice=[('M','Male'),('F','Female')]
	gender = forms.ChoiceField(choices=genderchoice, widget=forms.RadioSelect())
	
	countrychoice=[('1','India'),('2','USA'),('3','UK')]
	country = forms.ChoiceField(choices=countrychoice, widget=forms.Select())
	
	def clean_mobile(self):
		cd = self.cleaned_data
		mobile = cd.get('MobileNo')
		
		if len(mobile) != 10:
			raise forms.ValidationError("Please input a right mobile number")
		return mobile
	
	#RegistrationId = forms.AutoField(primary_key=True)
	
		
		