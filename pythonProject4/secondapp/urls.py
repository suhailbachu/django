from django.urls import path

from secondapp import views

urlpatterns = [
 path("",views.home,name='home')
]
