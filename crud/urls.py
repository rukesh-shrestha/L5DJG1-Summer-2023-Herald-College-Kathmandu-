from django.urls import path

from .views import index,about,create,contacts,partData

urlpatterns = [
    path("",index,name="home"),
    path("about/",about),
    path("create/",create),
    path("<int:id>/",partData),
    path("contacts/",contacts)

   
    
]