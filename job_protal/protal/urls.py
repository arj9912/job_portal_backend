
from django.urls import path
from. import views

from rest_framework_nested.routers import DefaultRouter

router = DefaultRouter()

router.register('jobs', views.JobViewSet, basename='jobs')

urlpatterns = [
    
]

urlpatterns = urlpatterns + router.urls