from rest_framework.viewsets import ModelViewSet

from core.models import Raca
from core.serializers import RacaSerializer


class RacaViewSet(ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer
