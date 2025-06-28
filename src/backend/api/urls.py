from django.urls import path
from api.views import PontoAPIView, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ponto/', PontoAPIView.as_view(), name='ponto'),
]