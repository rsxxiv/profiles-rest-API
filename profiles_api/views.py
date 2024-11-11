from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Using HTTP methods as functions (get, post, put, patch, delete)',
            'Is Similar to a tradional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})