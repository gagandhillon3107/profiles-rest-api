from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    def get(self, request, format=None):
        an_apiview = ["1st Item","2nd Item"]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})

