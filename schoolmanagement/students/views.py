from builtins import id

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from http import HTTPStatus

# Create your views here:

# GET ALL THE STUDENTS API :
@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    studentsSerializers = StudentSerializer(students, many=True)

    return Response(studentsSerializers.data)

#CREATE A STUDENT:
@api_view(['POST'])
def studentCreate(request):
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data, status=HTTPStatus.CREATED)

#GET STUDENT BY ID:
def studentById(request, id):
    student = Student.objects.get(id=id)
    studentSeria = StudentSerializer(student, many=False)

    return Response(studentSeria, status=HTTPStatus.ACCEPTED)

