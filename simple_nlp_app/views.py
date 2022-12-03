from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionsSerializers, AnswerSerializers
from .models import Questions, Answer
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
