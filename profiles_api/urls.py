#Here we store the URLs for our API
#Going back to our profiles_project urls.py we include our urls profiles_api in our
#urlpatterns list of the root project url
#We add a new iport to the django.urls, called include
#include is a function we can use for including URLs from other apps in the root project
#urls file
#Below the urlpatterns we add "path('api/', include('profiles_api.urls'))"

from django.urls import path

from profiles_api import views

#New list variable and create a list of paths that map two views in our project
#'hello-view/' is the name of the URL whcih we map to the view.HelloApiView. and we call
#as_view() class

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]

#when we open our project first it checks for the matching base URL 'api/' in the profiles_project
#then it is going to pass anything on the right hand of the slash and try to match it
#in the next url.py profiles_api file
#then matches 'hello-view/', so the URL that is gonna map to our view is the web server address/API/hello-view
#when Django matches this URL then call the views.HelloApiView.as_view(), which is the standard function that we 
#call to convert our API view class 

#Basically Django REST framework will call this get function in theviews.py in profiles_api
#if a HTTP get request is made to our URL

#This is how we map a URL to an APIView in Django
#Next we can test the API View in the browser