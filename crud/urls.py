from django.urls import path

from .views import index,about,create,contacts,partData,deleteBlog,updateBlog

app_name="crud"
urlpatterns = [
    path("",index,name="home"),
    path("about/",about,name="about"),
    path("create/",create,name="create"),
    path("<int:id>/",partData,name="particular"),
    path("contacts/",contacts,name="contacts"),
    path("delete/<int:id>/",deleteBlog,name="deleteblog"),
    path("update/<int:id>/",updateBlog,name="updateblog")


   
    
]