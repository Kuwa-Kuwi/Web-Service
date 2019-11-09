from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from noise_log.models import NoiseLog
from noise_log.serializers import NoiseLogSerializer


def noise_logs_list(request):
    noise_logs = NoiseLog.objects.all()
    return render(
        request=request,
        template_name='noise_log/noise_log_list.html',
        context={'noise_logs': noise_logs}
    )


class CreateNoiseLog(CreateAPIView):
    serializer_class = NoiseLogSerializer
