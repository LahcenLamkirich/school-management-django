from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
# Create your views here:

# GET ALL THE STUDENTS API :
@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    studentsSerializers = StudentSerializer(students, many=True)

    return Response(studentsSerializers.data)

# now we have to create some students : using shell

GEATTTTTTTTTTTTTTTTT !
