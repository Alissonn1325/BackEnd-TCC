from rest_framework.viewsets import ModelViewSet

from core.models import Adocao
from core.serializers import AdocaoSerializer


class AdocaoViewSet(ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer
