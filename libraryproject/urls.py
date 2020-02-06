# Django projects usually grow and start containing more than one application. By having each application define its own URLs, and then importing each set of those into the project, it prevents the project urls.py from becoming bloated and hard to read/maintain.

"""libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
# from django.urls import path
from libraryapp.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraryapp.urls')),
]
