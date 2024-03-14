from rest_framework import serializers

from django.contrib.auth.models import User

from protal.models import Job

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:

        model = User
        fields = ["id", "name", "email", "password"]
    
    def get_name(self, obj):
        return obj.first_name +" "+ obj.last_name

class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Job
        fields = ["id", "user", "title", "description", "salary", "company", "email", "job_category", "job_type", "job_experience", "job_vancancy",  "job_deadline", "created_at", "updated_at"]
        
class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["user", "title", "description", "salary", "company", "email", "job_category", "job_type", "job_experience", "job_vancancy",  "job_deadline"]


class UpdateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "description", "salary", "company", "email", "job_category", "job_type", "job_experience", "job_vancancy",  "job_deadline"]        