from django.urls import path

from another_another_resume_builder.resume.views import EnglishView

app_name = "resume"
urlpatterns = [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    path("en", EnglishView.as_view()),
]
