from rest_framework.routers import DefaultRouter

from .views import (
    QuestionGenViewSet,
    AnswerGenViewSet,
    PersonaViewSet,
    VerticalViewSet,
    SalesPersonViewSet
)

simple_app_router = DefaultRouter()
simple_app_router.register('questions', QuestionGenViewSet)
simple_app_router.register('answer', AnswerGenViewSet)
simple_app_router.register('persona', PersonaViewSet)
simple_app_router.register('vertical', VerticalViewSet)
simple_app_router.register('sales-person', SalesPersonViewSet)
