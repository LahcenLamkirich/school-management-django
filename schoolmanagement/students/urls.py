from django.urls import path
from . import views
# Let's create first the views :

urlpatterns = [
    path('', views.studentList)
]