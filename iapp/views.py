from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import auth,messages
from django.contrib.auth.models import User
from iapp.models import Contact
from . import mylogic

# Create your views here.

def index(request):
    data = {'name': str(mylogic.var)}
   

    return render(request,'index.html',data)

    
def register(request):
    if request.method == "POST":
        handleusername1 = request.POST.get('handleusername')
        handlepassword2 = request.POST.get('handlepassword')
        user = auth.authenticate(username = handleusername1 , password = handlepassword2)
        
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else: 
            messages.info(request,"INVALID USERNAME AND PASSWORD")
            return redirect(register)
    else :
        return render(request, 'register.html')
    
def registerout(request):
    auth.logout(request)
    messages.info(request,"LOG OUT SUCCESSFULLY!")
    return redirect('/')


def handlesignup(request):
    if request.method == "POST":
        # 1. Check if we are even receiving data
        print("--- DEBUG: FORM WAS SUBMITTED ---")
        
        usernamesignup = request.POST.get("usernamesignup")
        emailsignup = request.POST.get("emailsignup")
        passwordsignup = request.POST.get("passwordsignup")
        password2signup = request.POST.get("password2signup")
        
        # 2. Print the actual data we got
        print(f"Username received: {usernamesignup}")
        print(f"Email received: {emailsignup}")
        print(f"Password 1: {passwordsignup}")
        print(f"Password 2: {password2signup}")

        # Check for None (This is the most common error)
        if usernamesignup is None:
            print("ERROR: Username is None! Check HTML input name.")
            return redirect('signup')

        if passwordsignup != password2signup:
            print("ERROR: Passwords do not match")
            messages.info(request,"PASSWORDS DO NOT MATCH")
            return redirect('signup')
            
        # If we get here, create the user
        try:
            myuser = User.objects.create_user(usernamesignup, emailsignup, passwordsignup)
            myuser.save()
            print("SUCCESS: User created and saved!")
            messages.success(request,"Signup SUCCESSFULLY!")
            return redirect('/')
        except Exception as e:
            print(f"CRITICAL ERROR SAVING USER: {e}")
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        desc = request.POST.get("message")
        contact = Contact(name=name,youremail=email,subject=subject,message=desc)
        contact.save()

        return redirect('/')
    
    return render(request, 'index.html')

    

