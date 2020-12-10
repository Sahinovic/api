from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""
    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview=[
            'Uses HTTP method as functions (get, post, patch, put, detete)',
            'Is similar to a traditional django views',
            'gives you most control over app logic',
            'is mapped manualy to url '
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})