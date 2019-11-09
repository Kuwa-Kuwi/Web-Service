from rest_framework.serializers import ModelSerializer

from noise_log.models import NoiseLog


class NoiseLogSerializer(ModelSerializer):
    class Meta:
        model = NoiseLog
        fields = ['timestamp', 'decibel']
