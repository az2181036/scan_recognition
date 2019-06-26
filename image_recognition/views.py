from .serializers import ImageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from .OCR_and_IMAGE import OCR,image_labels

# Create your views here.
class ImageView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [AllowAny]
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ImageSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        filePath = serializer.data['image_init']
        redata = dict()
        redata['info'] = image_labels(filePath)
        redata['image_init'] = filePath
        return Response(redata, status=HTTP_200_OK)

class WordView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [AllowAny]
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        redata = dict()
        data = request.data
        serializer = ImageSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        filePath = serializer.data['image_init']
        redata['info'] = OCR(filePath)
        redata['image_init'] = filePath
        return Response(redata, status=HTTP_200_OK)
