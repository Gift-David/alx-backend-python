from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MessageViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'message', MessageViewSet)
router.register(r'conversation', ConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
