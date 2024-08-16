from rest_framework.serializers import ModelSerializer

from core.models import Situacao

class SituacaoSerializer(ModelSerializer):
    class Meta:
        model = Situacao
        fields = "__all__"