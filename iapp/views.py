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
        usernamesignup =request.POST.get("usernamesignup","").strip()
        emailsignup =request.POST.get("emailsignup")
        passwordsignup =request.POST.get("passwordsignup","").strip()
        password2signup =request.POST.get("password2signup","").strip()

        if passwordsignup == password2signup:
            user = User.objects.create_user(usernamesignup,emailsignup,passwordsignup)
            user.save()
            messages.success(request,"Signup SUCCESSFULLY!")
            return redirect('/')
        else:
            messages.info(request,"USER ALREADY EXIST TRY SOMETHING UNIQUE! ")
            return redirect('/')
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

    

