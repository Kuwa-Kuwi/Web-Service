from django.shortcuts import render

from noise_log.models import NoiseLog


def noise_logs_list(request):
    noise_logs = NoiseLog.objects.all()
    return render(
        request=request,
        template_name='noise_log/noise_log_list.html',
        context={'noise_logs': noise_logs}
    )
