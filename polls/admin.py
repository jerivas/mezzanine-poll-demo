#-*- coding: utf-8 -*-
from django.contrib import admin

from mezzanine.core.admin import DisplayableAdmin

from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(DisplayableAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
