from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.news.models import News

class newsView(ListView):
    model = News
    template_name = "_base.html"
    context_object_name ='News_list'
    


