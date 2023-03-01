from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.pages.models import Pages
from apps.componentApp.models import ComponentsPages, Component,Pages
from apps.slider.models import Slider



def homeContentView(request):
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    menu_list = Pages.objects.all()
    slider_list = Slider.objects.all()
    context = { 'menu_list': menu_list,'slider_list': slider_list}
    return render(request, 'pages/content.html', context)

def contentView(request, slug):
    print('************************************************ slug: ',slug)
    menu_list = Pages.objects.all()
    req_page = Pages.objects.get(Slug=slug)
    print('--------------------------------------------------------------------------------req_page',req_page)
    print('rew_page_id::::::::::::::', req_page.id)
    component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
    print('component_list : ', component_list)
    slider_list = Slider.objects.all()
    page = Pages.objects.filter(Slug= slug)
    context = {'component_list': component_list,'menu_list': menu_list,'slider_list': slider_list}
    return render(request, 'pages/content.html', context)
 