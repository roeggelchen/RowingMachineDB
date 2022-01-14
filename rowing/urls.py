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
    
    path("rowingsession/", views.RowingSessionListView.as_view(), name="rowing_session_list"),
    path("rowingsession/create/", views.RowingSessionCreateView.as_view(), name="rowing_session_create"),
    path("rowingsession/detail/<int:pk>/", views.RowingSessionDetailView.as_view(), name="rowing_session_detail"),
    path("rowingsession/update/<int:pk>/", views.RowingSessionUpdateView.as_view(), name="rowing_session_update"),
    path("rowingsession/delete/<int:pk>/", views.RowingSessioneDeleteView.as_view(), name="rowing_session_delete"),
    path("rowingstroke/", views.RowingStrokeListView.as_view(), name="rowing_stroke_list"),
    path("rowingstroke/create/", views.RowingStrokeCreateView.as_view(), name="rowing_stroke_create"),
    path("rowingstroke/detail/<int:pk>/", views.RowingStrokeDetailView.as_view(), name="rowing_stroke_detail"),
    path("rowingstroke/update/<int:pk>/", views.RowingStrokeUpdateView.as_view(), name="rowing_stroke_update"),
    path("rowingstroke/delete/<int:pk>/", views.RowingStrokeDeleteView.as_view(), name="rowing_stroke_delete"),

]