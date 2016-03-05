from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm,SignUpForm
from django.conf import settings
# Create your views here.
# def home(request):
# 	return render(request,"home.html",{})

def home(request):
	title='Welcome'
	# if request.user.is_authenticated():
	# 	title="My Title %s"%(request.user)
	
	#add a form
	# if request.method=="POST":
	# 	print(request.POST)
	'''
	<QueryDict: {u'csrfmiddlewaretoken': [u'2jAcG40EySn9zZov9i6P8p6ega22Qgdj'], 
	u'email': [u''], u'full_name': [u'']}>
	'''
	form=SignUpForm(request.POST or None)
	context={
	    "title":title,
	    "form":form
	}
	if form.is_valid(): #forms.py's def and so on
	    #print(request.POST['email'])#not recommended
	    	    #it's overriding the saving the form the clean data its actually not been validated here.

	    instance=form.save(commit=False)
	    full_name=form.cleaned_data.get("full_name")
	    if not full_name:
	    	full_name="New full name"
	    instance.full_name=full_name
	    #if not instance.full_name
	    #instance.full_name="Justin"
	    instance.save()
	    context={
	        "title":"Thank You"
	    }
	    #print(instance.email)
	    #print(instance.timestamp)

	return render(request,"example_fluid.html",context)

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		# for key,value in form.cleaned_data.iteritems():
		# 	print(key,value)
		#print(form.cleaned_data)
		form_email=form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")
		# print(email,message,full_name)
		subject='Site Contact form'
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email,'ilikecpp2010@163.com']
		contact_message="%s:%s via %s"%(
			form_full_name,
			form_message,
			form_email)

		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			fail_silently=True)


	context={
	    "form":form,
	}
	return render(request,"forms.html",context)