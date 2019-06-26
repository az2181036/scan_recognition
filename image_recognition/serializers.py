from drf_base64.serializers import ModelSerializer
from rest_framework.serializers import ImageField
from drf_base64.fields import Base64ImageField

from .models import ImageItems

class ImageSerializer(ModelSerializer):
    image_init = ImageField(required = True)
    image_end = ImageField(required = False)

    class Meta:
        model = ImageItems
        fields = "__all__"

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
