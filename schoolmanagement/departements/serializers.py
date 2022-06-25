from rest_framework import serializers
from .models import Departement


class DepartementSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Departement
        fields = '__all__'
