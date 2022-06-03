from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def profApi(request):
    return Response("Prof Api test")

#GET ALL PROFS :