from django.urls import path
from .views import *

urlpatterns = [
    path("sensors/", SensorView.as_view()),
    path("measurement/", MeasurementView.as_view()),
    path("sensor/<pk>/", SensorUpdate.as_view()),
]
