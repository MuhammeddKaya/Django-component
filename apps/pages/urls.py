from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homeContentView, name='home'),
    path('<slug:slug>/', views.contentView, name='page'),

]
