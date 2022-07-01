from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Professor
from .serialezers import ProfessorSerializer
from http import HTTPStatus


# Create your views here.

#GET ALL PROFS :
@api_view(['GET'])
def allProfs(request):
    professors = Professor.objects.all()
    print("Here ")
    profsSerializers = ProfessorSerializer(professors, many=True)

    return Response(profsSerializers.data, status=HTTPStatus.ACCEPTED)

#GET PROF BY ID :
@api_view(['GET'])
def getProfById(request, pk):
    prof = Professor.objects.get(id=pk)
    profSer = ProfessorSerializer(prof, many=False)

    return Response(profSer.data,status=HTTPStatus.ACCEPTED)

#POST PROF :
@api_view(['POST'])
def createProf(request):
    prof = ProfessorSerializer(data=request.data)
    if prof.is_valid():
        prof.save()

    return Response(prof.data, status=HTTPStatus.CREATED)

# DELETE PROF
@api_view(['DELETE'])
def deleteProf(request, pk):
    prof = Professor.objects.get(id=pk)
    if prof.delete():
        return Response('Professor Deleted Succesfully !')
    else:
        return Response('Professeur not deleted !!')
