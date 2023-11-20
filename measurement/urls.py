from django.urls import path

from measurement.views import SensorView, SensorOneView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorOneView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
