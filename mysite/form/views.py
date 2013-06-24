# Create your views here.
# Create your views here.
from django.shortcuts import render
#from forms import ContactForm
from django.http import HttpResponse
from mysite.form.models import regit
from mysite.form.forms import Register
#from django.template.context import Context
#from django.template.loader import get_template

def reg(request):
    new_obj = Register() 
    if request.method == 'POST':
        new_obj = Register(request.POST)
        if new_obj.is_valid():
            #new_obj.clean_data
            #cd.save(commit=False)
            new_obj.save()   
            return HttpResponse('Successfully registered')
    else:
        new_obj = Register()
    return render(request, 'form.html', {'form': new_obj})
            