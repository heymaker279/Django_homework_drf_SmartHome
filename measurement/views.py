from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, AllSensorSerializer, MeasurementSerializer


class SensorDetails(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    #
    # def patch(self, request):
    #     return Response({'status': 'OK'})


class AllSensors(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AllSensorSerializer


class MeasurementView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def post(self, request, *args, **kwargs):
    #     response = Measurement.objects.create(**kwargs)
    #     return Response(response)
