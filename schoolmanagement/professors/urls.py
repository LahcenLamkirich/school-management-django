from django.urls import path
from . import views
urlpatterns = [
    path('', views.profApi),
    path('prof-list', views.allProfs),
    path('profById/<str:pk>', views.getProfById)
]