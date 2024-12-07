from django.urls import path

from appnewtodo import views

urlpatterns = [
path("",views.home,name='home'),
path("todoadd",views.TodoAdd,name='TodoAdd'),
path("todoview",views.Todo_view,name='Todo_view'),
path("delete/<int:id>/",views.delete_data,name="delete"),
path("update/<int:id>/",views.update_data,name="update")
]