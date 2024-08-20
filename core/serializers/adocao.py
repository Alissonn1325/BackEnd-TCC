from rest_framework.serializers import ModelSerializer

from core.models import Adocao


class AdocaoSerializer(ModelSerializer):
    class Meta:
        model = Adocao
        fields = "__all__"
