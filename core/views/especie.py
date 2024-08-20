from rest_framework.viewsets import ModelViewSet

from core.serializers import EspecieSerializer
from core.models import Especie

class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class =EspecieSerializer