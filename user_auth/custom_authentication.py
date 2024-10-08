from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
import jwt
from .models import CustomUser

class CustomAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/") or request.path.endswith("/nt/") or request.path.startswith("/media") or request.path.startswith("/images"):
            request.thisUser = None
            response = self.get_response(request)
            return response

        token = request.headers.get('x-access-token')

        if not token:
            return JsonResponse({"Error": "Credentials Not Found. Please Login"}, status=status.HTTP_403_FORBIDDEN)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({"Error": "Token has expired"}, status=status.HTTP_403_FORBIDDEN)
        except jwt.InvalidTokenError:
            return JsonResponse({"Error": "Invalid Token"}, status=status.HTTP_403_FORBIDDEN)
        
        user = CustomUser.objects.filter(email=payload["id"]).first()
        request.thisUser = user
        response = self.get_response(request)
        return response