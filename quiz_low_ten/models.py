# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_low_ten'
    players_per_group = None
    num_rounds = 1
    point_per_correct = c(1.6)
    endowment = c(10)
    # correct answer for pre-test
    question11_correct = c(69.97)
    question12_correct = c(10)
    question13_correct = c(79.97)
    question21_correct = c(78.41)
    question22_correct = c(5)
    question23_correct = c(83.41)
    question31_correct = c(83.83)
    question32_correct = c(0)
    question33_correct = c(83.83)
    question4_correct = c(5)
    question5_correct = c(4)
    question6_correct = c(5)


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question11 = models.CurrencyField()
    question12 = models.CurrencyField()
    question13 = models.CurrencyField()
    question21 = models.CurrencyField()
    question22 = models.CurrencyField()
    question23 = models.CurrencyField()
    question31 = models.CurrencyField()
    question32 = models.CurrencyField()
    question33 = models.CurrencyField()
    question4 = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )
    question5 = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )
    question6 = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )


    def question11_correct(self):
        return self.question11 == Constants.question11_correct
    def question12_correct(self):
        return self.question12 == Constants.question12_correct
    def question13_correct(self):
        return self.question13 == Constants.question13_correct

    def question21_correct(self):
        return self.question21 == Constants.question21_correct
    def question22_correct(self):
        return self.question22 == Constants.question22_correct
    def question23_correct(self):
        return self.question23 == Constants.question23_correct

    def question31_correct(self):
        return self.question31 == Constants.question31_correct
    def question32_correct(self):
        return self.question32 == Constants.question32_correct
    def question33_correct(self):
        return self.question33 == Constants.question33_correct

    def question4_correct(self):
        return self.question4 == Constants.question4_correct

    def question5_correct(self):
        return self.question5 == Constants.question5_correct

    def question6_correct(self):
        return self.question6 == Constants.question6_correct

    def count_correct_questions(self):
        self.num_correct_questions = ( int(self.question11_correct()) + int(self.question12_correct()) + int(self.question13_correct()) + int(self.question21_correct())
                            + int(self.question22_correct()) + int(self.question23_correct()) + int(self.question31_correct()) + int(self.question32_correct())
                            + int(self.question33_correct()) + int(self.question4_correct()) + int(self.question5_correct()) + int(self.question6_correct())
                            )
        return self.num_correct_questions
    def set_payoff(self):
        self.payoff = Constants.point_per_correct * self.count_correct_questions()
        return self.payoff
