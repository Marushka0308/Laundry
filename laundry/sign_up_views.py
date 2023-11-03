from .models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User

@api_view(['GET','POST'])
def sign_up(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            response_data = {
                'success': True,
                'details': user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error': 'Invalid user data','errors': serializer.errors},status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'},status=400)


@api_view(['GET','PUT','DELETE','POST'])
def sign_up_detail(reqeust, id, format=None):
    try:
        users = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if reqeust.method == 'GET':
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    elif reqeust.method == 'PUT':
        serializer = UserSerializer(users, data = reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif reqeust.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif reqeust.method == 'POST':
        users.save()
        serializer = UserSerializer(users)
        return Response(serializer.data)

