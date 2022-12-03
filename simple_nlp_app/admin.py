from django.contrib import admin

from .models import Questions, Answer

admin.site.register(Questions)
admin.site.register(Answer)