from rest_framework import serializers
from student.models import Todo

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