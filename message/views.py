from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Message

# def message_views (request):
#     return render(request,'home.html')

class MessageView(ListView):
    model = Message
    template_name =  'home.html'
