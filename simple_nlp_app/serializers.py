from rest_framework import serializers
from .models import Questions, Answer


class QuestionsSerializers(serializers.ModelSerializer):
    """
    Serializer class to get questions
    """

    class Meta:
        model = Questions
        fields = [
            'types',
            'questions',
        ]


class AnswerSerializers(serializers.ModelSerializer):
    """
    Serializer class for Answer
    """

    class Meta:
        model = Answer
        fields = [
            'question',
            'number'
        ]
