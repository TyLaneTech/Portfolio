from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse 
from .forms import ContactForm
from django.shortcuts import redirect
from django.template.loader import get_template
from .models import Message


def contact(request):
	if request.method == 'POST':
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
			message=Message()
			message.name= request.POST.get('name')
			message.email= request.POST.get('email')
			message.message= request.POST.get('message')
			message.save()		
			print("success")	
			return render(request, 'message_sent.html')  
		else:
			return render(request,'contact.html')
	else:
		return render(request, "contact.html", {})




	
