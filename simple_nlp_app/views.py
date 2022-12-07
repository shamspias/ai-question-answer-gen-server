from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    QuestionsSerializers,
    AnswerSerializers,
    VerticalSerializers,
    PersonaSerializers,
    SalesPersonSerializers
)
from .models import Questions, Answer, Vertical, Persona, SalesPerson
from .task import generate_questions, generate_answers


class QuestionGenViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Generate Questions
    """

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        context = generate_questions(data['number'], data['types'], data['sales_person'], data['vertical'],
                                     data['persona'], data['questions'])
        return Response(context, status=status.HTTP_201_CREATED, )


class AnswerGenViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Get Answer
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        context = generate_answers(data['number'], data['types'], data['sales_person'], data['vertical'],
                                   data['persona'], data['question'])
        return Response(context, status=status.HTTP_201_CREATED, )


class PersonaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Get Persona
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers
    permission_classes = [permissions.AllowAny, ]


class VerticalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Get Vertical
    """
    queryset = Vertical.objects.all()
    serializer_class = VerticalSerializers
    permission_classes = [permissions.AllowAny, ]


class SalesPersonViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Get SalesPerson
    """
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializers
    permission_classes = [permissions.AllowAny, ]
