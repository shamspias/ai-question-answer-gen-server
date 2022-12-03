from rest_framework.routers import DefaultRouter

from .views import (
    QuestionGenViewSet,
    AnswerGenViewSet
)

simple_app_router = DefaultRouter()
simple_app_router.register('questions', QuestionGenViewSet)
simple_app_router.register('answer', AnswerGenViewSet)
