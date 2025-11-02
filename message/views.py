from django.shortcuts import render
from django.views.generic import TemplateView



# def message_views (request):
#     return render(request,'home.html')

class MessageView(TemplateView):
    template_name =  'home.html'
