#This is the entry point for all of the URLs in our app

"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#path is the item that links up the admin URL to the admin app
#This is created and enabled when we create a Django project
#When we head to the admin/ looks up our urls.py file and matches it with the first URL that it finds
#when we put an admin/ it detects this and then it passes the URL (admin.site.urls) for the admin site
#which connects that URL to the admin app that is included with Django by default

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]

#We will create a new urls.py file for our profiles_api app