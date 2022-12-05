from rest_framework import serializers
from .models import Questions, Answer, Persona, Vertical, SalesPerson


class QuestionsSerializers(serializers.ModelSerializer):
    """
    Serializer class to get questions
    """

    class Meta:
        model = Questions
        fields = "__all__"


class AnswerSerializers(serializers.ModelSerializer):
    """
    Serializer class for Answer
    """

    class Meta:
        model = Answer
        fields = "__all__"


class PersonaSerializers(serializers.ModelSerializer):
    """
    Serializer class for Persona
    """

    class Meta:
        model = Persona
        fields = "__all__"


class VerticalSerializers(serializers.ModelSerializer):
    """
    Serializer class for Vertical
    """

    class Meta:
        model = Vertical
        fields = "__all__"


class SalesPersonSerializers(serializers.ModelSerializer):
    """
    Serializer class for SalesPerson
    """

    class Meta:
        model = SalesPerson
        fields = "__all__"
