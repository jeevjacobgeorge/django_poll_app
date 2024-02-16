from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return(Student.objects.create(**validated_data))
    
    def update(self,instance , validated_data):
        instance.name = validated_data('name ', instance.name)
        instance.roll = validated_data('roll ', instance.roll)
        instance.city = validated_data('city ', instance.city)
        instance.save()
        return instance
    