from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'list_view')
            return redirect('accounts:dashboard')
        else:
            messages.error(
                request,
                "Username Or Password is incorrect!",
                extra_tags='alert alert-warning alert-dismissible fade show'
            )

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password1 != password2:
                e_tag = 'alert alert-warning alert-dismissible fade show'
                check1 = True
                messages.error(
                    request,
                    'Password did not match!',
                    extra_tags=e_tag
                )
            if User.objects.filter(username=username).exists():
                e_tag = 'alert alert-warning alert-dismissible fade show'
                check2 = True
                messages.error(
                    request,
                    'Username already exists!',
                    extra_tags=e_tag
                )
            if User.objects.filter(email=email).exists():
                e_tag = 'alert alert-warning alert-dismissible fade show'
                check3 = True
                messages.error(
                    request,
                    'Email already registered!',
                    extra_tags=e_tag
                )

            if check1 or check2 or check3:
                e_tag = 'alert alert-warning alert-dismissible fade show'
                messages.error(
                    request,
                    "Registration Failed!",
                    extra_tags=e_tag
                )
                return redirect('accounts:register')
            else:
                e_tag = 'alert alert-success alert-dismissible fade show'
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request,
                    f'Thanks for registering {user.username}.',
                    extra_tags=e_tag
                )
                return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def payment_page(request):
    return render(request, 'accounts/payment_page.html')


def newsletter(request):
    return render(request, 'accounts/newsletter.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
