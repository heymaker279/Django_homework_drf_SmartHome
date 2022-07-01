
from django.urls import path
from measurement.views import SensorDetails, AllSensors, MeasurementView

urlpatterns = [
    path('sensors/', AllSensors.as_view()),
    path('sensors/<pk>/', SensorDetails.as_view()),
    path('measurements/', MeasurementView.as_view()),
]