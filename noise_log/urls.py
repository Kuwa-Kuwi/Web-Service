from django.urls import path

from noise_log.views import noise_logs_list

app_name = 'noise_log'
urlpatterns = [
    path('all/', noise_logs_list, name='noise-logs-list'),
]
