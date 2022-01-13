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
    
    path("polls/rowingsession/", views.playerListView.as_view(), name="rowing_session_list"),
    path("polls/rowingsession/create/", views.playerCreateView.as_view(), name="rowing_session_create"),
    path("polls/rowingsession/detail/<int:pk>/", views.playerDetailView.as_view(), name="rowing_session_detail"),
    path("polls/rowingsession/update/<int:pk>/", views.playerUpdateView.as_view(), name="rowing_session_update"),
    path("polls/rowingsession/delete/<int:pk>/", views.playerDeleteView.as_view(), name="rowing_session_delete"),
    path("polls/rowingstroke/", views.matchListView.as_view(), name="rowing_stroke_list"),
    path("polls/rowingstroke/create/", views.matchCreateView.as_view(), name="rowing_stroke_create"),
    path("polls/rowingstroke/detail/<int:pk>/", views.matchDetailView.as_view(), name="rowing_stroke_detail"),
    path("polls/rowingstroke/update/<int:pk>/", views.matchUpdateView.as_view(), name="rowing_stroke_update"),
    path("polls/rowingstroke/delete/<int:pk>/", views.matchDeleteView.as_view(), name="rowing_stroke_delete"),

]