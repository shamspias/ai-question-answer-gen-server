from django.contrib import admin

from .models import Persona, Vertical, SalesPerson, ConversationalDirection

admin.site.register(Persona)
admin.site.register(Vertical)
admin.site.register(SalesPerson)
admin.site.register(ConversationalDirection)
