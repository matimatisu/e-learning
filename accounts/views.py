from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')

    return render(
        request,
        'accounts/login.html'
    )

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
