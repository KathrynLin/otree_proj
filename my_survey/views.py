# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = models.Player
    form_fields = ['q_lottery_instruction1',
                    'q_lottery_instruction2',
                    'q_lottery_instruction3',
                    'q_lottery_instruction4']

class Lottery_instruction(Page):
    form_model = models.Player
    form_fields = ['q_lottery_instruction1',
                    'q_lottery_instruction2',
                    'q_lottery_instruction3',
                    'q_lottery_instruction4']


# class Lottery_instruction(Page):
#     form_model = models.Player
#     form_fields = ['q_lottery_instruction1']
    #               'q_lottery_instruction2',
    #               'q_lottery_instruction3',
    #               'q_lottery_instruction4',
    #               ]

class Lottery(Page):
    form_model = models.Player
    form_fields = ['q_lottery1',
                  'q_lottery2',
                  'q_lottery3',
                  'q_lottery4',
                  'q_lottery5',
                  'q_lottery6',
                  'q_lottery7',
                  'q_lottery8',
                  'q_lottery9',
                  'q_lottery10',
                  'q_lottery_instruction1',
                  'q_lottery_instruction2',
                  'q_lottery_instruction3',
                  'q_lottery_instruction4'
                  ]
    def before_next_page(self):
        self.player.set_payoff()



class Results(Page):
    def vars_for_template(self):

        lottery_payoff = self.player.payoff
        payoff_so_far = self.player.participant.payoff
        decision_for_payment = self.session.vars['paying_choice']
        die_num = self.session.vars['die']

        return {
            'decision_for_payment': decision_for_payment,
            'die_num': die_num,
            'choice_for_payment': self.player.choice_list()[self.session.vars['paying_choice'] - 1],
            'payment': lottery_payoff.to_real_world_currency(self.session),
            'payoff_so_far': payoff_so_far,
            'payoff_so_far_money': payoff_so_far.to_real_world_currency(self.session)
            }


class Survey(Page):
    form_model = models.Player
    form_fields = ['q_country',
                  'q_age',
                  'q_gender',
                  'q_ethnic',
                  'q_marriage',
                  'q_employ',
                  'q_student',
                  'q_education',
                  'q_major',
                  'q_siblings',
                  'q_vote',
                  'q_job',
                  'q_income',
                  'q_instruction1',
                  'q_instruction2',
                  'q_instruction3',
                  'q_instruction4',]


page_sequence = [
    Introduction,
    Lottery,
    Results,
    Survey
]

# page_sequence = [
#     Lottery_instruction,
#     Lottery,
#     Results
# ]
