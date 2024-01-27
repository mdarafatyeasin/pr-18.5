from typing import Any
from django.shortcuts import render,redirect
# from . import forms
from .forms import RegisterForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



# registration 
def userRegistration(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account created successfully!!!')
            register_form.save()
            return redirect('homePage')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form':register_form, 'type':'Registration'})

# login
def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Welcome back!!!')
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('sign_up')
    else:
        login_form = AuthenticationForm()
    return render(request, 'register.html', {'form': login_form, 'type': 'LogIn'})

# logout
def log_out(request):
    messages.warning(request, 'Please Login first')
    logout(request)
    return redirect('homePage')


# change user data 
@login_required #login required
def profile(request):
    data = Post.objects.filter(author= request.user)
    return render(request, 'profile.html', {'data':data})

# change password 
@login_required
def pass_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            messages.success(request, "Password Changed")
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form': form})

# edit profile
def edit_profile(request):
    if request.method == "POST":
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            messages.success(request, "User updated")
            form.save()
            return redirect('profile')
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form':form})


# login
class login_views(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('homePage')

    def form_valid(self, form):
        messages.success(self.request, 'Welcome back from class')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Login information incorrect!!!')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


class logout_view(LogoutView):
    def get_success_url(self):
        return self.get_redirect_url('homePage')