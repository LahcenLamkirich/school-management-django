from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Professor
from .serialezers import ProfessorSerializer
from http import HTTPStatus
# Create your views here.
@api_view(['GET'])
def profApi(request):
    return Response("Prof Api test")

#GET ALL PROFS :
def allProfs(request):
    professors = Professor.objects.all()
    profsSerializers = ProfessorSerializer(professors, many=True)

    return Response(profsSerializers.data, status=HTTPStatus.ACCEPTED)

def getProfById(request, pk):
    prof = Professor.objects.get(id=pk)
    profSer = ProfessorSerializer(prof, many=False)

    return Response(profSer.data,status=HTTPStatus.ACCEPTED)

