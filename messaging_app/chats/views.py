from rest_framework import viewsets
from . serializers import UserSerializer, MessageSerializer, ConversationSerializer
from . models import User, Message, Conversation

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class ConversationViewset(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    

