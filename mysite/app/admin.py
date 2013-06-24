from django.contrib import admin
from mysite.app.models import FormData



class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email', 'country')
    #list_filter = ('country')
    

admin.site.register(FormData, FormDataAdmin)
