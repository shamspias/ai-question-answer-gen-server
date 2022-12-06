from django.db import models


class Questions(models.Model):
    """
    questions body Model
    """
    types = models.CharField(max_length=40, blank=True, null=True)
    number = models.IntegerField(default=1)
    sales_person = models.CharField(max_length=250, blank=True, null=True)
    vertical = models.CharField(max_length=250, blank=True, null=True)
    persona = models.CharField(max_length=250, blank=True, null=True)
    questions = models.TextField(blank=True, null=True)


class Answer(models.Model):
    """
    Answer model
    """
    types = models.CharField(max_length=40, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    sales_person = models.CharField(max_length=250, blank=True, null=True)
    vertical = models.CharField(max_length=250, blank=True, null=True)
    persona = models.CharField(max_length=250, blank=True, null=True)
    number = models.IntegerField(default=1)
    answer = models.TextField(blank=True, null=True)


class ConversationalDirection(models.Model):
    """
    To create and set information
    """
    categories = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.categories


class Persona(models.Model):
    """
    Model for Persona
    """
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Vertical(models.Model):
    """
    Model for Vertical
    """
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class SalesPerson(models.Model):
    """
    Model for Vertical
    """
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
