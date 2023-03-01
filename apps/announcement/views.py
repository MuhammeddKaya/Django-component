from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.announcement.models import Announcement

class announcementView(ListView):
    model= Announcement
    #template_name = "_base.html"
    context_object_name ='announcement_list'
