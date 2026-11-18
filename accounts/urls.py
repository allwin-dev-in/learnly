from django.urls import path

from accounts.views import SignupView
from accounts.views import UserRetriveUpdateDeleteView

urlpatterns=[
    path("signup/",SignupView.as_view()),
    path("user/edit/<int:pk>/",UserRetriveUpdateDeleteView.as_view()),

]