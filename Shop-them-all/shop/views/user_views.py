from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from ..forms import RegisterForm
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




    def get_user_from_form(self, request):

        user = {}
        user['email'] = request.POST['email']
        user['password'] = request.POST['password']
        user['confirmPassword'] = request.POST['confirmPassword']
        user['first_name'] = request.POST['first_name']
        user['last_name'] = request.POST['last_name']
        user['country'] = request.POST['country']
        user['birthday'] = request.POST['birthday']
        user['sex'] = request.POST['sex']
        return user

    def is_valid_user(self, user):
            if User.objects.filter(email=user['email']).exists():
                # treat this case later
                pass

            if user['password'] != user['confirmPassword']:
                # treat this case later
                pass

            return True