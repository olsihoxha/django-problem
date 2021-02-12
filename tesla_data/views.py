from rest_framework.generics import ListCreateAPIView
from .models import CountryName1, TeslaModel1
from .serializers import TeslaModelSerializer, CountryNameSerializer


class TeslaModelListCreateAPIView(ListCreateAPIView):
    queryset = TeslaModel1.objects.all()
    serializer_class = TeslaModelSerializer


class CountryNameListCreateAPIView(ListCreateAPIView):
    queryset = CountryName1.objects.all()
    serializer_class = CountryNameSerializer
