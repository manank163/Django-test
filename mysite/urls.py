from django.conf.urls.defaults import patterns, include, url
from app.views import contact, login_view , logout_view , home
from form.views import reg
from django.contrib.auth import login,logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact/$',contact),
    url(r'^form/$',reg), 
    url(r'^login/$',  login_view),
    url(r'^logout/$', logout_view),
    url(r'^home/$',home),
    #url(r'^color/$',show_color),         
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)
