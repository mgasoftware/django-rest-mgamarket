from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from item.models import Item
from .serializers import ItemSerializer, MyTokenObtainPairSerializer, RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ItemList(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        category = self.request.query_params.get('category')

        if category is not None:
            queryset = queryset.filter(category=category) 
        return queryset
    
class ItemDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

# class ConversationList(ListCreateAPIView):
#     serializer_class = ConversationSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = Conversation.objects.all()

# class ConversationDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = ConversationSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = Conversation.objects.all()