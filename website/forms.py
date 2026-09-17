from django import forms
from website.models import Contact, newslatters
from captcha.fields import CaptchaField

class Contact_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        

class Newslatter_form(forms.ModelForm):

    class Meta:
        model = newslatters
        fields = '__all__'


