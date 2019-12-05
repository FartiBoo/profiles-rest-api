from rest_framework import serializers

#class HelloSerializer and base it on the serialized class from the Django REST framework. The .Serializers is a class
#we create a simple serializer that accepts a name input and then add this to our API View and use it to test the post 
#functionality of our APIView
#In a serializer you specify the fields that you want to accept in your serializer input
#we create a field called name and this is a value that can be passed into the request that will be validated by the serializer
#Serializer also takes care of validation rules, so if we want to accept a certain field or a certain type serializer will make
#sure that the content pass the API is of the correct type 

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

    #this creates a new name field on our serializer which is a character field that allows us to input any text on the computer 
    #and gives maximum length of 10



