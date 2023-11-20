# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorOneSerializer


class SensorView(generics.ListCreateAPIView): # Получение датчиков и создание

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorOneView(generics.RetrieveUpdateAPIView): # Получение информации по датчику и обновление
    queryset = Sensor.objects.all()
    serializer_class = SensorOneSerializer


class MeasurementsView(generics.CreateAPIView): # Добавление измерения

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer