from django import forms

class ContactForm(forms.Form):
	#name = forms.CharField(max_length=100)
	#email = forms.EmailField()
	#password = forms.CharField(min_length=7, widget=forms.PasswordInput())
	#dob = forms.DateField()
	#genderchoice=[('Male','Male'),('Female','Female')]
	#gender = forms.ChoiceField(choices=genderchoice, widget=forms.RadioSelect())
	#mob =  forms.CharField(max_length=10)
	#genderchoice1=[('1','India'),('2','USA'),('3','UK')]
	#country = forms.ChoiceField(choices=genderchoice1, widget=forms.Select())from django import forms
	
	#RegistrationId = forms.AutoField(primary_key=True)
	
	EmailId = forms.EmailField("Email Id", max_length=30)
	FirstName = forms.CharField("First Name", max_length=50)
	LastName = forms.CharField("Last Name", max_length=50)
	Password = forms.PasswordInput("Password", max_length=10)
	MobileNo = forms.CharField("Mobile Number", max_length=15)
	
	def clean_mobile(self):
		cd = self.cleaned_data
		mobile = cd.get('MobileNo')
		
		if len(mobile) != 10:
			raise forms.ValidationError("Please input a right mobile number")
		return mobile
	
			
		
	
	
	