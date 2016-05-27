# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import math
import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Yingzhi Liang'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 3
    endowment = c(100)
    efficiency_factor = 1.8
    rho = 0.5
    beta = 2

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
       # self.total_contribution = sum([p.contribution for p in self.get_players()])
       # self.individual_share =  self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        self.total_contribution = sum([math.pow(p.contribution,Constants.rho) for p in self.get_players()] )
        self.individual_share = Constants.beta * math.pow(self.total_contribution,float(1)/Constants.rho)
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share



class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)