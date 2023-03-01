from django.shortcuts import render
from apps.slider.models import Slider
# Create your views here.


def sliderView(request):

    context = {'slider_list': slider_list}
    return render(request, 'pages/content.html', context)


