# Create your views here.
from django.shortcuts import render
#from forms import ContactForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from mysite.app.models import FormData
#from mysite.app.forms import ContactForm
from django.template.context import Context
from django.template.loader import get_template
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout


def contact(request):
    
    contact_sent = request.session.get('contact_sent',False)
    
    if request.method == "GET":
        html = get_template("contact_form.html")
        response = html.render(Context())
        return HttpResponse(response)
    
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print "WORKED"
    else:
        print "did not work"
              
    if request.method == "POST":
        EmailId = request.POST['email']
        Password = request.POST['pwd']
        confpass = request.POST['confpwd']
        Name = request.POST['name']
        MobileNo = request.POST['mob']
        gender = request.POST['gender']
        country = request.POST['country']
        dob = request.POST['dob']
        
        r = FormData();
        r.email=EmailId;
        r.Password=Password;
        r.name=Name;
        r.confpass = confpass;
        r.MobileNo=MobileNo;
        r.gender=gender;
        r.country=country;
        r.dob = dob;
        r.save()
        request.session["contact_sent"]= True
        
        request.session.set_test_cookie()
        return HttpResponse("Successfully Registered.")

def login_view(request):
    state = "please log in below"
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None: 
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/home')
            else:
                state = "your account is not active"
        else:
            state = "wrong userid / password "
    return render(request, 'login.html', {'state':state})

def logout_view(request):
    auth_logout(request)
    return HttpResponse("logged out")

def home(request):
    if request.method == "GET":
        html = get_template("homepage.html")
        response = html.render(Context())
        return HttpResponse(response)

#def my_image(request):
#    image_data = open ( "/static/facebook.png","rb").read()
#    return HttpResponse(image_data, mimetype= "facebook.png")


        
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             new_obj = form.save(commit=False)
#             new_obj.save()
#             return HttpResponse('/thanks/')
#         else:
#             form = ContactForm ()
#             return render(request, 'contact_form.html', {'form': form})