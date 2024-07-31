from rest_framework.serializers import ModelSerializer

from core.models import Adotante


class AdotanteSerializer(ModelSerializer):
    class Meta:
        model = Adotante
        fields = "__all__"
