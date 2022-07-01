from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Departement
from .serializers import DepartementSerializer

# Create your views here.

#GET ALL THE DEPARTEMENTS :
@api_view(['GET'])
def allDepartements(request):
    try:
        departements = Departement.objects.all()
        depaSerializer = DepartementSerializer(departements, many=True)
        return Response(depaSerializer.data)
    except Departement.DoesNotExist:
        return("No Data Found !")

#CREATE A DEPARTEMENT
@api_view(['POST'])
def createDepartement(request):
    departement = DepartementSerializer(data=request.data)
    if departement.is_valid():
        departement.save()

    return Response(departement.data)

