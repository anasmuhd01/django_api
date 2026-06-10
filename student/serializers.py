from rest_framework import serializers

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