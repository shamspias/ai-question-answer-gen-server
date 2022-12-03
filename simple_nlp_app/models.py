from django.db import models


class Questions(models.Model):
    """
    questions body Model
    """
    types = models.CharField(max_length=40, blank=True, null=True)
    questions = models.TextField(blank=True, null=True)


class Answer(models.Model):
    """
    Answer model
    """
    question = models.TextField(blank=True, null=True)
    number = models.IntegerField(default=1)
    answer = models.TextField(blank=True, null=True)
