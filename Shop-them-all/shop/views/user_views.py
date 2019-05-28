from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from ..forms import RegisterForm, LogInForm
from django.views.decorators.csrf import csrf_exempt



class SignUpView(View):


    def post(self, request, *args, **kwargs):

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')



        return render(request, 'register.html', {'form': form})


    def get(self,request, *args, **kwargs):

        form = RegisterForm()
        return render(request, 'register.html', {'form': form})



# class MyLoginView(LoginView):
#     template_name = 'login.html'
#     form_list = (
#         ('auth', LogInForm()),
#         # ... the rest from the original here ...
#     )