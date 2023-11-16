from django.urls import path

from measurement.views import SensorView, SensorOneView

#baseUrl = 'http://localhost:8000/api'
urlpatterns = [
    path('api/sensor', SensorView.as_view()),
    path('api/sensor/<pk>', SensorOneView.as_view()),
    path('api/measurements', SensorView.as_view()),
]
