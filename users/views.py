from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerUser(request):
    if request.method== "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        if password == confirmpassword:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                password=password
            )
            user.save()
            return redirect("crud:home")
        else:
            print("password validation failed")
        

    return render(request,"users/register.html")

def loginUser(request):
    if(request.user.is_authenticated):
        return redirect("crud:home")
    else:

        print(request.user)
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("crud:home")
            else:
                print("User Validation Failed - 401")
                return redirect("users:signin")
        return render(request,"users/login.html")

@login_required
def logoutUser(request):
    logout(request)
    return redirect("crud:home")



