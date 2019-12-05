#Import APIView class from the rest_framework.views module
#the REST framework is the django rest famework we installed previously in the requirements.txt file

from rest_framework.views import APIView

#Import the Response object which is used to return responses from the APIView
#It is a standard Response object that when we call the APIView or when Django REST framework
#calls our APIView, expects to return the standard Response object

from rest_framework.response import Response

#APIView class - this creates a new class based on the APIView class that the Django REST framework provides
#It allows us to define the application logic for our endpoint that we can assign to this view
#The way this works is that we define a URL which is our endpoint
#Then we assign it to the View and the Django REST framework handles it by calling a function in the View
#for the HTTP request that you make

#ADD POST METHOD TO APIVIEW --------- 

#the status objects from the rEST framework is a list of HTTP status codes that we can use when returning responses from our API

from rest_framework import status

#serializer module we created in the serializers.py
#we use this module to tell our APIView what data to expect when making post input and patch requests to our API

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    #ADD POST METHOD TO APIVIEW --------- 

    #We set the serializer 
    #This configures our API View to have the serializer class we created in serializers.py

    serializer_class = serializers.HelloSerializer 

    #We will accept a HTTP get request to our API
    #HTTP get request: used to retrieve a list of objects or a specific object, so whenever we make a HTTP get request
    #to the URL, then it will be assigned to this APIView and call the get function
    #and it will execute the logic that we write in the get function
    #the parameters are self, which is required for all class functions, a request object, which is passed by Django
    #REST framework and contains details of the request being made to the API
    #and the format which is used to add a format suffix to the end of the endpoint URL
    #We will not use the format, but it is best practice to keep it in here
    #In the def function we will define a list which describes all the features of an APIView
    #get, post, patch, put, delete are functions that we can add to our API to support the different HTTP requests
    #an_apiview is a simple list that shows how an APIView works in practice, it doesn't maatter the content
    #it is just for demonstrating the return of an object in our APIView
    #Every function added to an APOView that is a HTTP function, like get, post, patch, put, delete, must return
    #a response object. Django REST framework expects it to return a response which will then output as part when 
    #the API is called
    #The response needs to contain a dictionary or a list which is will be outputed when the API is called
    #It converts the response object to Json and in order to convert it to Json it needs to be either a list or 
    #a dictionary
    #we are gonna return a dictionary and ad a key called 'message' with a string value 'hello' and a second key 
    #'an_apiview' and pass our an_apiview

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'messages': 'Hello', 'an_apiview': an_apiview})

#Now that we have our APIView we can wire it up to our URL in Django
#We have a urls.py file in the root of our profiles_project directory, this is the entry point for all the URLs in our app

#ADD POST METHOD TO APIVIEW --------- 
#We add the post function to our API View
#We will create a hello message when we receive a post request to our Hello API
#Then we will retrieve the serializer and pass in the data that was sent in the request
#self.serializer_class function is a function that comes with the API View that retrieves the configured serialized class for our view
#It is the standard way that we should retrieve the serialized class
#the data=request.data assigns the data, we assign this data to our serialized class and then we create a new variable for our serialized 
#class called serializer (serializer=self.serializer_class(data=request.data))

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

#now we can validate the serializer. Django REST framework as mentioned provides the functionality to validate the input
#that means that the input is validated for our serializers.py requirements, in this case that the name is no longer than 10 characters
#it will retrieve the name field we defined

    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        message = f'Hello {name}'
    return Response({'message': message})
    else:
        return Response(
        erializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

#if the input is not valid we retunr a HTTP 400 bad request to Response
#serializer.errors returns a dictionary of all the errors based on the validation rules that were applied to the serializer