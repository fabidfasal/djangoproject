from django.shortcuts import render,redirect
from . forms import SignUpForm,LoginForm,ChangePasswordForm,UpdateForm
from . models import Table1
from django .contrib import messages
from django .contrib.auth import logout as logouts

# Create your views here.
def index(request):
    return render(request,'index.html')




def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            user=Table1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,'user already exists')
                return redirect('/signup')
            elif password!=password:
                messages.warning(request,'mismatched')
                return redirect('/signup')
            else:
                tab=Table1(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"complete")
                return redirect("/")
    else:
        form=SignUpForm()
    return render(request,'signup.html',{'data':form}) 





def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Table1.objects.get(Email=email)

                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'incorrect password')
                    return redirect('/login')
                else:
                    messages.success(request,"login success")
                    return redirect('/user_home/%s' % user.id)
            except:
                messages.success(request,"incorrect email or password")
                return redirect("/login")
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form}) 



def user_home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'user_home.html',{"data":user})


def profile(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'profile.html',{"data":user})



def changepassword(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            cpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                messages.warning(request,"password incorrect")
                return redirect('/changepassword/%s' % user.id)
            
            elif newpassword==oldpassword:
                messages.warning(request,'same password')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=cpassword:
                    messages.warning(request,'incorrect password')
                    return redirect('/changepassword/%s' % user.id)


            else:
                    user.Password=newpassword
                    user.save()
                    messages.success(request,"password changed succefully")
                    return redirect("/user_home")
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user}) 


def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():

         form.save()
         messages.success(request,"update succefully")
         return redirect('/user_home')

    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})


def logout(request):
    logouts(request)
    messages.success(request,'logout succeefull') 
    return redirect('/')