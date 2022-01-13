from rest_framework import viewsets, permissions

from . import serializers
from . import models


class RowingSessionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rowing Session class"""

    queryset = models.RowingSession.objects.all()
    serializer_class = serializers.RowingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class RowingStrokeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rowing Stroke class"""

    queryset = models.RowingStroke.objects.all()
    serializer_class = serializers.RowingStrokeSerializer
    permission_classes = [permissions.IsAuthenticated]
