from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from protal.serializers import CreateJobSerializer, JobSerializer, UpdateJobSerializer

from protal.models import Job

# Create your views here.

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    # serializer_class = JobSerializer

    def get_serializer_class(self):
        if self.request.method=="POST":
            return CreateJobSerializer
        elif self.request.method=="PUT":
            return UpdateJobSerializer
        return JobSerializer

