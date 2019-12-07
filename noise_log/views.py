import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from noise_log.models import NoiseLog
from noise_log.serializers import NoiseLogSerializer


def noise_logs_list(request):
    return render(
        request=request,
        template_name='noise_log/noise_log_list.html'
    )


def get_noise_logs(request):
    noise_logs = NoiseLog.objects.all()
    noise_logs_serialized = NoiseLogSerializer(instance=noise_logs, many=True).data
    data = json.dumps({'logs': noise_logs_serialized})
    return HttpResponse(content=data, content_type='application/json')


class CreateNoiseLog(CreateAPIView):
    serializer_class = NoiseLogSerializer
