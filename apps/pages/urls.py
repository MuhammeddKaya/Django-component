from django.urls import path
from . import views
from django.urls import path, re_path


app_name = 'pages'

urlpatterns = [
    path('', views.homeContentView, name='home'),
    path('<slug:slug>/', views.contentView, name='page'),


]
