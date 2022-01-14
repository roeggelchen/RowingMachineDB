from rest_framework import serializers

from . import models


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
            "question_text",
            "pub_date"
        ]
        
class RowingSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RowingSession
        fields = [
            "comport",
            "c",
            "t",
            "version",
            "max_level",
            "h",
            "start_time",
            "end_time"
        ]

class RowingStrokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RowingStroke
        fields = [
            "rowing_session",
            "t",
            "distance",
            "one",
            "speed",
            "strokes_per_minute",
            "watts",
            "colories_per_hour",
            "zero",
            "level",
            "message",
            "time_stamp"
        ]
