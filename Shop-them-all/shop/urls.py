from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LogInForm

from django.urls import path

from . import views

urlpatterns = [url(r'^$', views.home, name='home'),
			   url(r'^register$', views.SignUpView.as_view(), name='register'),
			   url(r'^login$', LoginView.as_view(template_name='login.html',  authentication_form = LogInForm, redirect_authenticated_user=True), name="login"),
			   url(r'^logout', LogoutView.as_view(), name="logout"),
			   url(r'^product', views.get_prduct_details, name="product"),

			   ]