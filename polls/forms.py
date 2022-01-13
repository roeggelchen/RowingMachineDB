from django import forms
from . import models


class RowingSessionForm(forms.ModelForm):
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


class RowingStrokeForm(forms.ModelForm):
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
