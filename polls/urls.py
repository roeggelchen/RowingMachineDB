from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register("rowingsession", api.RowingSessionViewSet)
router.register("rowingstroke", api.RowingStrokeViewSet)

urlpatterns = [
    path('', views.index, name='index'),

    path("api/v1/", include(router.urls)),
    
    path("polls/rowingsession/", views.RowingSessionListView.as_view(), name="rowing_session_list"),
    path("polls/rowingsession/create/", views.RowingSessionCreateView.as_view(), name="rowing_session_create"),
    path("polls/rowingsession/detail/<int:pk>/", views.RowingSessionDetailView.as_view(), name="rowing_session_detail"),
    path("polls/rowingsession/update/<int:pk>/", views.RowingSessionUpdateView.as_view(), name="rowing_session_update"),
    path("polls/rowingsession/delete/<int:pk>/", views.RowingSessioneDeleteView.as_view(), name="rowing_session_delete"),
    path("polls/rowingstroke/", views.RowingStrokeListView.as_view(), name="rowing_stroke_list"),
    path("polls/rowingstroke/create/", views.RowingStrokeCreateView.as_view(), name="rowing_stroke_create"),
    path("polls/rowingstroke/detail/<int:pk>/", views.RowingStrokeDetailView.as_view(), name="rowing_stroke_detail"),
    path("polls/rowingstroke/update/<int:pk>/", views.RowingStrokeUpdateView.as_view(), name="rowing_stroke_update"),
    path("polls/rowingstroke/delete/<int:pk>/", views.RowingStrokeDeleteView.as_view(), name="rowing_stroke_delete"),

]