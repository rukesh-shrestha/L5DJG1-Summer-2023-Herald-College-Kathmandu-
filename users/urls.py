from django.urls import path,include

from .views import registerUser,loginUser,logoutUser


app_name="users"
urlpatterns = [
    path("register/",registerUser,name="signup"),
    path("login/",loginUser,name="signin"),
    path("logout/",logoutUser,name="signout"),
  
    
]