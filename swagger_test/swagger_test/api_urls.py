from django.urls import path, include
from rest_framework import routers

from post.views import PostViewSet


router = routers.SimpleRouter()
router.register('post', PostViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
