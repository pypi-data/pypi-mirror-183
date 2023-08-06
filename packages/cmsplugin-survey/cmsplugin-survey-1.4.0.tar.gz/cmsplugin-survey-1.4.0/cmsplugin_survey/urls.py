from django.urls import path

from . import views

app_name = "survey"

urlpatterns = [
    path("vote/<int:question_id>/", views.vote, name="vote"),
]
