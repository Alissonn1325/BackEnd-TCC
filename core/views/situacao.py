from rest_framework.viewsets import ModelViewSet

from core.models import Situacao
from core.serializers import SituacaoSerializer

class SituacaoViewSet(ModelViewSet):
    queryset = Situacao.objects.all().order_by("id")
    serializer_class = SituacaoSerializer