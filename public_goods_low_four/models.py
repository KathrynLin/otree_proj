# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
import math
import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Yingzhi Liang'

doc = """
This is a twenty period public goods game with 4 players. The production
function is the constant elasticity of substitution function. Players are
rematched at the start of each period. In this game, rho = 0.7, beta = 0.4,
omega = 10, n = 4.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_low_four'
    players_per_group = 4
    num_rounds = 20
    other_player_per_group = players_per_group - 1

    #"""Amount allocated to each player"""
    rho = 0.7
    beta = 0.4
    endowment = c(10)





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

        if self.round_number == 1:
            paying_round = random.sample(range(1, 21), 1)
            self.session.vars['paying_round'] = paying_round




class Group(BaseGroup):

    group_income = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.individual_share = Constants.beta * math.pow(sum([math.pow(p.contribution,Constants.rho) for p in self.get_players()]),float(1)/Constants.rho)
        self.group_income = self.individual_share * Constants.players_per_group

        for p in self.get_players():
            if self.subsession.round_number in self.session.vars['paying_round']:
                p.payoff = Constants.endowment - p.contribution + self.individual_share
            else:
                p.payoff = c(0)

            p.payoff_each_round = Constants.endowment - p.contribution + self.individual_share



class Player(BasePlayer):

    payoff_each_round = models.CurrencyField()
    contribution = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )
