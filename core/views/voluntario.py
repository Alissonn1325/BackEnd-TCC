from rest_framework.viewsets import ModelViewSet

from core.models import Voluntario
from core.serializers import VoluntarioSerializer


class VoluntarioViewSet(ModelViewSet):
    queryset = Voluntario.objects.all
    serializer_class = VoluntarioSerializer
