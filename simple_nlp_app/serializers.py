from rest_framework import serializers
from .models import Questions, Answer, Persona, Vertical, SalesPerson, ConversationalDirection


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


# class ConversationalDirectionSerializer(serializers.ModelSerializer):
#     """
#     Serializer class for Answer Category
#     """
#
#     class Meta:
#         model = ConversationalDirection
#         fields = ['categories', ]


class PersonaSerializers(serializers.ModelSerializer):
    """
    Serializer class for Persona
    """
    categories = serializers.SlugRelatedField(
        read_only=True,
        slug_field="categories"
    )

    class Meta:
        model = Persona
        fields = ['name', 'categories']


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
