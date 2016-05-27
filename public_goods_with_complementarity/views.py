# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class Introduction(Page):

    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.subsession.round_number == 1

class Question(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = models.Player
    form_fields = ['question11','question12','question13',
    'question21','question22','question23','question31','question32','question33','question4','question5','question6' ]


class Feedback(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class Contribute(Page):

    """Player: Choose how much to contribute"""

    form_model = models.Player
    form_fields = ['contribution']

    #timeout_submission = {'contribution': c(Constants.endowment/2)}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


class Results(Page):

    """Players payoff: How much each has earned"""

    def vars_for_template(self):

        return {
            'total_earnings': self.group.total_contribution * Constants.efficiency_factor,
            'individual_earnings': self.player.payoff
        }

page_sequence = [Introduction,
            Question,
            Feedback,
            Contribute,
            ResultsWaitPage,
            Results]
