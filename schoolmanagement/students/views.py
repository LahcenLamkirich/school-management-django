from builtins import id

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from http import HTTPStatus
from django.shortcuts import render

# Create your views here:

# GET ALL THE STUDENTS API :
@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    studentsSerializers = StudentSerializer(students, many=True)
    context = {
        'name': "Lahcen"
    }
    return render(request, "students/index.html", context)
    # return Response(studentsSerializers.data)

#CREATE A STUDENT:
@api_view(['POST'])
def studentCreate(request):
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data, status=HTTPStatus.CREATED)

#GET STUDENT BY ID:
@api_view(['GET'])
def studentById(request, pk):
    student = Student.objects.get(id=pk)
    studentSeria = StudentSerializer(student, many=False)

    return Response(studentSeria.data, status=HTTPStatus.ACCEPTED)

#DELETE STUDENT
@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response("Student deleted successfully !")

