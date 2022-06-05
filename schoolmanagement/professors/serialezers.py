from rest_framework import serializers
from .models import Professor
class ProfessorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    matiere = serializers.CharField(max_length=50)

    class Meta:
        model = Professor
        fields = '__all__'