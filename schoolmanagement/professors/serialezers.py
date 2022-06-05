from rest_framework import serializers

class ProfessorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    matiere = serializers.CharField(max_length=50)

