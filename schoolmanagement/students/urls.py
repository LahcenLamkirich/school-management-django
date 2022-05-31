from django.urls import path
from . import views

# Let's create first the views :

urlpatterns = [
    path('', views.studentList),
    path('create-student', views.studentCreate),
    path('delete-student/<str:pk>', views.deleteStudent),
    path('studentById/<str:pk>', views.studentById)
]