from django.contrib import admin

from .models import Questions, Answer, Persona, Vertical, SalesPerson

admin.site.register(Questions)
admin.site.register(Answer)


admin.site.register(Persona)
admin.site.register(Vertical)
admin.site.register(SalesPerson)
