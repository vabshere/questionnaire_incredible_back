from django.urls import path

from question_manager import views

urlpatterns = [
    path(
        "generate_questionnaire/",
        views.generate_questionnaire,
        name="generate_questionnaire",
    ),
]
