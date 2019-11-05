"""slimeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from core.views import splash, login_, logout_, signup_, create_slimeline, create_event, display_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", splash, name="splash"),
    path("login", login_, name="login"),
    path("logout", logout_, name="logout"),
    path("signup", signup_, name="signup"),
    path("create_slimeline", create_slimeline, name="create_slimeline"),
    path("create_event", create_event, name="create_event"),
    path("display_event", display_event, name="display_event"),
]
