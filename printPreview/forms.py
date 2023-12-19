from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class Signupform(UserCreationForm):
    fullname = forms.CharField(max_length=50,required=True)
    external_no = forms.IntegerField(required=True)

    class Meta:
        model=User
        fields = ('fullname','external_no','username','password1','password2')


# -------------------- Response Section ----------------------
# form for response Table
class Response_Form(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
        exclude = ['request_id','response_id']   
                 


# Response_activites  
# class Response_activites_Form(forms.ModelForm):
#     class Meta:
#         model = Response_activites
#         fields = '__all__'     




# Response_attachments  
# class Response_attachments_Form(forms.ModelForm):
#     class Meta:
#         model = Response_attachments
#         fields = ['attachment_display_name']
 


# # Response_external_entites  
# class Response_external_entites_Form(forms.ModelForm):
#     class Meta:
#         model = Response_external_entites
#         fields = ['comments','entity_decision']     
