from rest_framework import viewsets
from . serializers import UserSerializer, MessageSerializer, ConversationSerializer
from . models import User, Message, Conversation
from . pagination import StandardResultsSetPagination
from .filters import MessageFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.filter()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends  = [MessageFilter]
    permission_classes = ["IsAuthenticated", "HTTP_403_FORBIDDEN"]
    
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    

# "conversation_id"