from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Animal


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
        foto_attachment_key = SlugRelatedField(
            source="foto",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
    )
    foto = ImageSerializer(
        required=False,
        read_only=True
    )
