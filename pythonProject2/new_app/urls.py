from django.urls import path

from new_app import views

urlpatterns = [
    path("test",views.test,name="test")


]
