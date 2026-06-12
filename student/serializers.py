from rest_framework import serializers
from student.models import *

class AssignmentSerializer(serializers.Serializer):
    title=serializers.CharField()
    description = serializers.CharField()
    added_at = serializers.DateTimeField(read_only=True)
    submission_date = serializers.DateField( )

class TodoSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    added_at = serializers.DateTimeField(read_only=True)
    subject = serializers.CharField() 

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ['added_at']

    
class TeachreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def validate(self, attrs):
        print(attrs)
        age = attrs.get('age')
        if age<18:
            raise serializers.ValidationError("Age Must Be greater Than 18")
        return super().validate(attrs)