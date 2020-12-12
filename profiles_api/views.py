from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview=[
            'Uses HTTP method as functions (get, post, patch, put, detete)',
            'Is similar to a traditional django views',
            'gives you most control over app logic',
            'is mapped manualy to url '
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """creating a hello msg with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk = None):
        """handel updating an objesct"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handel partial update"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """deliting object"""

        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """test api viesets"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """return hello msg"""

        a_viewset= [
            'users action(list, create,retrive, update, partial update,',
            'automaticky maps to urls using routers',
            'provides more funcionality with less code'
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}!'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle geting a object by its ID"""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """update an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """partial update of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """removing object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating an updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)