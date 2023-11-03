from .models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def login(request, format = None):
    if request.method == 'POST':
        name = request.data.get('name')
        password = request.data.get('password')

        try:
            user = User.objects.get(name=name, password=password)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid name or password'},status=400)

        user_data = UserSerializer(user).data
        response_data = {
            'success': True,
            'details': user_data
        }
        return JsonResponse(response_data, status = 200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
