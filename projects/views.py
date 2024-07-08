from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSerializer
from django.utils.decorators import method_decorator
from .decorators import validate_country

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    
    # def start_survey(self, request):
    #     return Http
    @action(detail=True, methods=['post'], url_path='start-survey', permission_classes=[AllowAny])
    @method_decorator(validate_country)
    def start_survey(self, request, pk=None):
        remoteIP = request.META.get('REMOTE_ADDR')
        print("remoteIP ", remoteIP, request.data.get("country"))
        project = self.get_object()
        print("project ", project)
        # Add your logic here to start the survey
        project.state = 'started'
        project.save()
        return Response({'status': 'survey started'}, status=status.HTTP_200_OK)