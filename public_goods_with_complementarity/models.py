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
This is a twenty period public goods game with 4 players. The production
function is the constant elasticity of substitution function. Players are
rematched at the start of each period.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_with_complementarity'
    players_per_group = 4
    num_rounds = 20
    other_player_per_group = players_per_group - 1

    #"""Amount allocated to each player"""
    rho = 0.5
    beta = 2
    endowment = c(10)

    # correct answer for pre-test
    question11_correct = c(5)
    question12_correct = c(5)
    question13_correct = c(5)
    question21_correct = c(4)
    question22_correct = c(4)
    question23_correct = c(4)
    question31_correct = c(3)
    question32_correct = c(3)
    question33_correct = c(3)
    question4_correct = c(2)
    question5_correct = c(1)
    question6_correct = c(0)



class Subsession(BaseSubsession):

    def before_session_starts(self):
        players = self.get_players()
        random.shuffle(players)

        group_matrix = []

        # chunk into groups of Constants.players_per_group
        ppg = Constants.players_per_group
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i + ppg])
        self.set_groups(group_matrix)


class Group(BaseGroup):

    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([math.pow(p.contribution,Constants.rho) for p in self.get_players()] )
        self.individual_share = Constants.beta * math.pow(self.total_contribution,float(1)/Constants.rho)
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share


class Player(BasePlayer):


    contribution = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )

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
