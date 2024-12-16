from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def register_user(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    if not name or not email or not password:
        return Response(
            {"message": "Todos os campos (name, email, password) são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if "@" not in email or "." not in email.split("@")[-1]:
        return Response(
            {"message": "Endereço de email inválido."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(name=name).exists():
        return Response(
            {"message": "Já existe um usuário com este nome de usuário."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"message": "Já existe um usuário com este email."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.create_user(name=name, email=email, password=password)
        response_data = {
            "message": "Usuário criado com sucesso!",
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {"message": f"Erro ao criar usuário: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
