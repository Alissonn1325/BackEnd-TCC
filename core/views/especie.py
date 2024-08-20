from rest_framework.viewsets import ModelViewSet

from core.models import Especie
from core.serializers import EspecieSerializer


class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
