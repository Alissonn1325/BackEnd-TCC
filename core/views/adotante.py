from rest_framework.viewsets import ModelViewSet

from core.models import Adotante
from core.serializers import AdotanteSerializer


class AdotanteViewSet(ModelViewSet):
    queryset = Adotante.objects.all()
    serializer_class = AdotanteSerializer
