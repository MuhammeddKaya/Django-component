from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.newsView.as_view(), name='news'),

]
