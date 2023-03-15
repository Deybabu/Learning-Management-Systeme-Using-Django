from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def sample(request: HttpRequest) -> HttpResponse:
    """
    DOCS: This is sample function.

        :args: request
        :returns: HttpResponse
    """
    mth = None
    if request.method == 'GET':
        mth = 'GET'
    else:
        mth = 'POST'
    return HttpResponse(f"Hello, {mth}")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username, password)
        x = authenticate(username=username, password=password)
        if x is None:
            return redirect(reverse('core:welcome-page'))
        else:
            print('login successfull')
            login(request, x)
            return redirect(reverse('core:welcome-page'))
    return render(request, 'user/login.html', context={})


def user_register(request):
    pass


def user_logout(request):
    pass
