from django.urls import path
from .views import *

urlpatterns = [
    path('send-daily-report/', DailyReportEmailAPIView.as_view(), name='send_daily_report'),
]
