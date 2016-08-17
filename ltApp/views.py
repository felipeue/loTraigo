from django.shortcuts import render
from ltApp.forms import UserForm, UserLtForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        userlt_form = UserLtForm(data=request.POST)
        passconfirm = request.POST.get('pass')
        if user_form.is_valid() and userlt_form.is_valid():
            user = user_form.save()
            if user.password == passconfirm:
                user.set_password(user.password)
                user.save()
                userlt = userlt_form.save(commit=False)
                userlt.userOrigin = user
                userlt.save()
                registered = True
        else:
            print userlt_form.errors, user_form.errors
    else:
        user_form = UserForm()
        userlt_form = UserLtForm()
    return render(request, 'register.html', {'user_form': user_form, 'userlt_form': userlt_form, 'registered': registered})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponse("You account is disabled")
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'login.html', {})


@login_required
def dashboard(request):
    return render(request, 'index_dashboard.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
