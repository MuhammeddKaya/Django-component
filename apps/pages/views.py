from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
import webbrowser
from apps.pages.models import Pages
from apps.componentApp.models import ComponentsPages, Component,Pages
from apps.slider.models import Slider
from django.http import HttpResponseRedirect



# def contentView(request, slug=''):
#     if not slug:
#         menu_list = Pages.objects.all()
#         req_page = Pages.objects.get(Slug='home')
#         component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
#         layout_list = Pages.objects.get(Slug='home')
#         #layout_list = Pages.objects.filter(Page_id = req_page.id )
#         print('Slug is None')
#         menu_list = Pages.objects.all()
#         slider_list = Slider.objects.all()
#         context =  {'component_list': component_list,
#                     'layout_list': layout_list,
#                     'menu_list': menu_list,
#                     'slider_list': slider_list,
#                     #'componentsPagesHeader': component_list.filter(ComponentLocation='01H').order_by('ComponentOrder').all(),
#                     'componentsPagesLeft': component_list.filter(ComponentLocation='02L').order_by('ComponentOrder').all(),
#                     'componentsPagesContent': component_list.filter(ComponentLocation='03C').order_by('ComponentOrder').all(),
#                     'componentsPagesRight': component_list.filter(ComponentLocation='04R').order_by('ComponentOrder').all(),}
#         return render(request, 'pages/content_copy.html', context)
#     else:

#         print('Else kısmı caliştı ',slug)
#         menu_list = Pages.objects.all()
#         req_page = Pages.objects.get(Slug=slug)
#         print('--------------------------------------------------------------------------------req_page',req_page)
#         print('rew_page_id::::::::::::::', req_page.id)
#         component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
#         layout_list = Pages.objects.get(Slug=slug)
#         print('layout_list : ', layout_list)
#         slider_list = Slider.objects.all()
#         context = {'component_list': component_list,
#                    'layout_list': layout_list,
#                    'menu_list': menu_list,
#                    'slider_list': slider_list,
#                     'componentsPagesLeft': component_list.filter(ComponentLocation='02L').order_by('ComponentOrder').all(),
#                     'componentsPagesContent': component_list.filter(ComponentLocation='03C').order_by('ComponentOrder').all(),
#                     'componentsPagesRight': component_list.filter(ComponentLocation='04R').order_by('ComponentOrder').all(),}
#         return render(request, 'pages/content_copy.html', context)
    


def contentView(request, slug=''):
        if not slug:
            menu_list = Pages.objects.all()
            req_page = Pages.objects.get(Slug='home')
            component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
            layout_list = Pages.objects.get(Slug='home')
            #layout_list = Pages.objects.filter(Page_id = req_page.id )
            print('Slug is None')
            menu_list = Pages.objects.all()
            slider_list = Slider.objects.all()
            context =  {'component_list': component_list,
                        'layout_list': layout_list,
                        'menu_list': menu_list,
                        'slider_list': slider_list,
                        #'componentsPagesHeader': component_list.filter(ComponentLocation='01H').order_by('ComponentOrder').all(),
                        'componentsPagesLeft': component_list.filter(ComponentLocation='02L').order_by('ComponentOrder').all(),
                        'componentsPagesContent': component_list.filter(ComponentLocation='03C').order_by('ComponentOrder').all(),
                        'componentsPagesRight': component_list.filter(ComponentLocation='04R').order_by('ComponentOrder').all(),}
            return render(request, 'pages/content_copy.html', context)
        else:
            #req_page = Pages.objects.get(Slug=slug)
            if Pages.objects.get(Slug=slug).Link is not None:
                req_link=Pages.objects.get(Slug=slug)
                print('linkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk:::',req_link.Link)
                webbrowser.open_new_tab(req_link.Link)
                #return HttpResponseRedirect(request.META.get(''))
                return redirect(reverse('pages:home'))
            else:

                print('Else kısmı caliştı ',slug)
                menu_list = Pages.objects.all()
                req_page = Pages.objects.get(Slug=slug)
                print('--------------------------------------------------------------------------------req_page',req_page.Link)
                print('rew_page_id::::::::::::::', req_page.id)
                component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
                layout_list = Pages.objects.get(Slug=slug)
                print('layout_list : ', layout_list)
                slider_list = Slider.objects.all()
                context = {'component_list': component_list,
                        'layout_list': layout_list,
                        'menu_list': menu_list,
                        'slider_list': slider_list,
                            'componentsPagesLeft': component_list.filter(ComponentLocation='02L').order_by('ComponentOrder').all(),
                            'componentsPagesContent': component_list.filter(ComponentLocation='03C').order_by('ComponentOrder').all(),
                            'componentsPagesRight': component_list.filter(ComponentLocation='04R').order_by('ComponentOrder').all(),}
                return render(request, 'pages/content_copy.html', context)

#Layout eklenmemiş hali

# def contentView(request, slug=''):
#     if not slug:
#         menu_list = Pages.objects.all()
#         req_page = Pages.objects.get(Slug='home')
#         component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
#         print('Slug is None')
#         menu_list = Pages.objects.all()
#         slider_list = Slider.objects.all()
#         context = {'component_list': component_list,'menu_list': menu_list,'slider_list': slider_list}
#         return render(request, 'pages/content.html', context)
#     else:

#         print('Else kısmı caliştı ',slug)
#         menu_list = Pages.objects.all()
#         req_page = Pages.objects.get(Slug=slug)
#         print('--------------------------------------------------------------------------------req_page',req_page)
#         print('rew_page_id::::::::::::::', req_page.id)
#         component_list = ComponentsPages.objects.filter(Page_id = req_page.id)
#         print('component_list : ', component_list)
#         slider_list = Slider.objects.all()
#         context = {'component_list': component_list,'menu_list': menu_list,'slider_list': slider_list}
#         return render(request, 'pages/content.html', context)

 