from rest_framework import serializers
from .models import Student

#obliged to do ModelSerializer and not serializer:
class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    class Meta:
        model = Student
        fields = '__all__'