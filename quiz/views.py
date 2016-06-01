# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return True

class Question(Page):

    def is_displayed(self):
        return True

    form_model = models.Player
    form_fields = ['question11','question12','question13',
    'question21','question22','question23','question31','question32','question33','question4','question5','question6' ]


class Feedback(Page):
    def is_displayed(self):
        return True

class Results(Page):

    """Players payoff: How much each has earned"""

    def is_displayed(self):
        return True


page_sequence = [Introduction,
            Question,
            Feedback,
            Results
            ]
