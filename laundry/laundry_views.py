from .models import Laundry
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LaundrySerializer
from rest_framework import status
from laundry.forms import UploadForm
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse


@api_view(['GET','POST'])
def laundry(request, format = None):
    if request.method == 'GET':
        laundry = Laundry.objects.all()
        serializer = LaundrySerializer(laundry, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LaundrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            laundry_data = serializer.data
            response_data = {
                'success': True,
                'details': laundry_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error': 'Invalid laundry data','errors': serializer.errors},status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'},status=400)

@api_view(['GET','PUT','DELETE','POST'])
def laundry_detail(request, id, format=None):

    try:
        laundry = Laundry.objects.get(pk=id)
    except Laundry.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaundrySerializer(laundry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaundrySerializer(laundry, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        laundry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        laundry.save()
        serializer = LaundrySerializer(laundry)
        return Response(serializer.data)

def home(request):
    return HttpResponse("ok")
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'laundry/upload.html', {'form': UploadForm})