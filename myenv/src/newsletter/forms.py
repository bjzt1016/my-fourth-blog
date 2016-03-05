from django import forms

from .models import SignUp

class ContactForm(forms.Form):#don't neccessarily depend on model
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['full_name','email']
		### exclude=['full_name']  use sparingly
	def  clean_email(self): ###self is the form in below pic.
		#print(self.cleaned_data) ###{'email': u'bbb@bbb.com', 'full_name': u''}
		email=self.cleaned_data.get('email')
		email_base,provider=email.split("@")
		domain,extension=provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address!")
		return email ###return at list
	def clean_full_name(self):
		full_name=self.cleaned_data.get('full_name')
		#write validation code.
		return full_name