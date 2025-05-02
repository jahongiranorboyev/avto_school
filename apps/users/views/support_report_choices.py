from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import Support


class ReportChoicesAPIView(APIView):
    def get(self, request):
        choices = [
            {"value": choice[0], "label": choice[1]}
            for choice in Support.Report.choices
        ]
        return Response(choices)