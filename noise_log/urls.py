from django.urls import path

from noise_log.views import noise_logs_list, CreateNoiseLog, get_noise_logs

app_name = 'noise_log'
urlpatterns = [
    path('all/', noise_logs_list, name='noise-logs-list'),
    path('get-noise-logs/', get_noise_logs, name='get-noise-logs'),
    path('create-noise-log/', CreateNoiseLog.as_view(), name='create-noise-log'),
]
