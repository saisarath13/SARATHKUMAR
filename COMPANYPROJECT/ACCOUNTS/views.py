from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import GeeksForm
from .models import GeeksModel


# Create your views here.





def REGISTER(request, user=True):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('REGISTER')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('REGISTER')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')

                return redirect('/')



        else:
            messages.info(request, 'password not matching')
            return redirect('REGISTER')
            return redirect('/')
    else:
        return render(request, 'REGISTER.html')





def upload(request):
    context = {}
    if request.method == "POST":
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            event = form.cleaned_data.get("event")
            img = form.cleaned_data.get("image")
            amount = form.cleaned_data.get("amount")
            obj = GeeksModel.objects.create(
                title=name,
                event=event,
                img=img,
                amount=amount
            )
            obj.save()
            print(obj)
            return redirect('/')
    else:
        form = GeeksForm()
    context['form'] = form
    return render(request, "BABA/Upload.html", context)




def painting(request):
    context = {}
    if request.method == "POST":
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            event = form.cleaned_data.get("event")
            img = form.cleaned_data.get("image")
            amount = form.cleaned_data.get("amount")
            obj = GeeksModel.objects.create(
                title=name,
                event=event,
                img=img,
                amount=amount
            )
            obj.save()
            print(obj)
            return redirect('/')
    else:
        form = GeeksForm()
    context['form'] = form
    return render(request, "BABA/painting.html", context)

def rules(request):

        return render(request, 'BABA/rules.html')


def rules1(request):
    return render(request, 'BABA/rules1.html')