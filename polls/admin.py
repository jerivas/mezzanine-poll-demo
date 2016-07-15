#-*- coding: utf-8 -*-
from django.contrib import admin

from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin

from .models import Choice, Poll


class ChoiceInline(TabularDynamicInlineAdmin):
    model = Choice
    readonly_fields = ('votes',)


class PollAdmin(DisplayableAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
