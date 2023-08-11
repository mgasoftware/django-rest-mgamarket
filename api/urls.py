from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('v1/item/', views.ItemList.as_view()),
    path('v1/item/<int:pk>/', views.ItemDetail.as_view()),
    # path('v1/chat/', views.ConversationList.as_view()),
    # path('v1/chat/<int:pk>/', views.ConversationDetail.as_view()),
]