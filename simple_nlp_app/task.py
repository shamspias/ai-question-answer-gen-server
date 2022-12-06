from celery import shared_task
from django.conf import settings

import openai


@shared_task(name='GenerateQuestions')
def generate_questions(number=1, types="short", person1="Sales Representative", vertical="AI", person2="CEO",
                       prompt=""):
    """
    Method to generate questions based on few questions from OpenAI using GPT3
    """
    openai.api_key = settings.OPEN_AI_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write {} {} questions where {} asking to {} about {} based on {}\n-".format(number, types, person1,
                                                                                            person2, vertical, prompt),
    temperature = 0.7,
    max_tokens = 256,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
    )
    my_text = response['choices'][0]['text'].split("\n")

    new_text = []

    for i, word in enumerate(my_text):
        if len(word) > 4:
            if word[0] == '-':
                new_text.append(word[1:])
            else:
                new_text.append(word)
    context = {
        'data': new_text
    }
    return context


@shared_task(name='GenerateAnswers')
def generate_answers(number=1, types="short", person1="Sales Representative", vertical="AI", person2="CEO",
                     prompt=""):
    """
    Method to generate questions from OpenAI using GPT3
    """
    openai.api_key = settings.OPEN_AI_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write {} {} answer as a {} given to {} about {} from \n {}\n-".format(number, types, person2,
                                                                                      person1, vertical, prompt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    my_text = response['choices'][0]['text'].split("\n")

    new_text = []

    for i, word in enumerate(my_text):
        if len(word) > 4:
            if word[0] == '-':
                new_text.append(word[1:])
            else:
                new_text.append(word)
    context = {
        'data': new_text
    }
    return context
