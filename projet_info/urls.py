"""
URL configuration for projet_info project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main.views import check_age
from django.shortcuts import redirect
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_age/', include('main.urls')),
    path('', lambda request: redirect('check_age')),  # Redirige vers /check_age/


    #Django auth trucs
    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout")
]

#path('accounts/', include('django.contrib.auth.urls'))

#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change-done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done'
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']