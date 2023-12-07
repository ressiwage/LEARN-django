from django.contrib import admin

from .models import Option


class ReadAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Option, ReadAdmin)