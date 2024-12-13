from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["patch"])
    def alterar_telefone(self, request, pk=None):
        usuario = self.get_object()
        serializer = UsuarioAtualizarTelefoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario.profile.telefone = serializer.validated_data["telefone"]
        usuario.profile.save()

        return Response(
            {"detail": f"Telefone do usuário '{usuario.username}' atualizado para {usuario.profile.telefone}."},
            status=status.HTTP_200_OK,
        )
