from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app1.utils import send_daily_report

class DailyReportEmailAPIView(APIView):
    def get(self, request):
        result = send_daily_report()
        return Response({"message": result}, status=status.HTTP_200_OK)
