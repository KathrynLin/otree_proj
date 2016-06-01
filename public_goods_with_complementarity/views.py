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

    def vars_for_template(self):

        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'player_in_all_rounds': self.player.in_all_rounds()
        }

    #timeout_submission = {'contribution': c(Constants.endowment/2)}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


class Results(Page):

    """Players payoff: How much each has earned"""

    def vars_for_template(self):

        return {
            'total_group_income': self.group.group_income,
            'earnings_from_private': Constants.endowment - self.player.contribution,
            'earnings_from_public': self.group.individual_share,
            'individual_earnings': self.player.payoff,
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'player_in_all_rounds': self.player.in_all_rounds()
        }

class FinalResult(Page):


    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        total_payoff = sum([p.payoff for p in player_in_all_rounds])
        total_payoff1 = self.player.participant.payoff


        return {'player_in_all_rounds': player_in_all_rounds,
                'total_payoff': total_payoff,
                'total_payoff_money': total_payoff1.to_real_world_currency(self.session),
                'total_plus_base': total_payoff + Constants.base_points}

# page_sequence = [Introduction,
#             Question,
#             Feedback,
#             Contribute,
#             ResultsWaitPage,
#             Results,
#             FinalResult]
page_sequence = [
            Contribute,
            ResultsWaitPage,
            Results,
            FinalResult]
