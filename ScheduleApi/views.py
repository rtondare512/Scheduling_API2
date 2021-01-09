from django.shortcuts import render
from .models import DT
from rest_framework.views import APIView
from .serializers import DTSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
import time
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
def TaskSchedule(request):
	taskserializer = DTSerializer(data=request.data) 
	if taskserializer.is_valid():
		taskserializer.save()
		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Schedule(request,url):
	taskurl = DT.objects.get(url=url)
	dt=taskurl.dt
	print(dt)
	current=time.strftime(r"%Y-%m-%d %H:%M:00+00:00", time.localtime()) 
	print(current)
	if str(dt)==str(current):
		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Ping(request):
	return Response({"status":"OK"})

