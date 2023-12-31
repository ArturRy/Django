from rest_framework import serializers

from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["sensor", "temperature", "created_at"]


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurement"]


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            "id",
            "name",
            "description",
        ]
