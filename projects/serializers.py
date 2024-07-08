from rest_framework import serializers
from .models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('created_by', 'updated_by')