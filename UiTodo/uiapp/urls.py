from django.urls import path

from uiapp import views

urlpatterns = [
   path("dude",views.dude,name='dude'),
   # path("add",views.add_list,name='add_list'),
   path("newin",views.newin,name='newin'),
   path("ModeAdd",views.ModeAdd,name='ModeAdd'),
   path("Mode_view",views.Mode_view,name='Mode_view'),
   path("delete/<int:id>/",views.delete_data,name="delete"),
   path("update/<int:id>/",views.update_data,name="update")


    ]