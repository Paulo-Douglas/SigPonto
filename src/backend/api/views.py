from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from api.serializers import PontoSerializer
from rest_framework.views import APIView
from api.models import Servidor, Ponto
from rest_framework import status

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        
        if not username:
            return Response({"error": "username é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            servidor = Servidor.objects.get(username=username)
        except Servidor.DoesNotExist:
            return Response({"error": "Servidor não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=servidor)
        return Response({"token": token.key, "username": servidor.username})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class PontoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PontoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        servidor = request.user
        pontos = Ponto.objects.filter(servidor=servidor).order_by('-data_hora')
        serializer = PontoSerializer(pontos, many=True)
        return Response(serializer.data)
