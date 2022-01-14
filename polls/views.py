from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Penis.")


class RowingSessionListView(generic.ListView):
    model = models.RowingSession
    form_class = forms.RowingSessionForm


class RowingSessionCreateView(generic.CreateView):
    model = models.RowingSession
    form_class = forms.RowingSessionForm


class RowingSessionDetailView(generic.DetailView):
    model = models.RowingSession
    form_class = forms.RowingSessionForm


class RowingSessionUpdateView(generic.UpdateView):
    model = models.RowingSession
    form_class = forms.RowingSessionForm
    pk_url_kwarg = "pk"


class RowingSessioneDeleteView(generic.DeleteView):
    model = models.RowingSession
    success_url = reverse_lazy("rowing_session_list")


class RowingStrokeListView(generic.ListView):
    model = models.RowingStroke
    form_class = forms.RowingStrokeForm


class RowingStrokeCreateView(generic.CreateView):
    model = models.RowingStroke
    form_class = forms.RowingStrokeForm


class RowingStrokeDetailView(generic.DetailView):
    model = models.RowingStroke
    form_class = forms.RowingStrokeForm


class RowingStrokeUpdateView(generic.UpdateView):
    model = models.RowingStroke
    form_class = forms.RowingStrokeForm
    pk_url_kwarg = "pk"


class RowingStrokeDeleteView(generic.DeleteView):
    model = models.RowingStroke
    success_url = reverse_lazy("rowing_stroke_list")
