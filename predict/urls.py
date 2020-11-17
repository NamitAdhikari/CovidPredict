from django.urls import path
from .views import PostRequest

urlpatterns = [
    path('', PostRequest, name='post-request')
]
