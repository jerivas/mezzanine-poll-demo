#-*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from mezzanine.core.models import Displayable, Orderable


class Poll(Displayable):

    def get_absolute_url(self):
        return reverse('polls:detail', args=[self.slug])


class Choice(Orderable):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
