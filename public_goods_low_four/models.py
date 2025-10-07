from otree.api import *
# <standard imports>
import math
import random

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
    endowment = 10





class Subsession(BaseSubsession):

    def creating_session(self):

        players = self.get_players()
        random.shuffle(players)

        group_matrix = []

        # chunk into groups of Constants.players_per_group
        ppg = Constants.players_per_group
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i + ppg])
        self.set_group_matrix(group_matrix)

        if self.round_number == 1:
            paying_round = random.sample(range(1, Constants.num_rounds + 1), 1)
            self.session.vars['paying_round'] = paying_round




class Group(BaseGroup):

    group_income = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        # Calculate individual share from group contributions
        contributions = [p.contribution if p.contribution is not None else 0 for p in self.get_players()]
        self.individual_share = Constants.beta * math.pow(sum([math.pow(c, Constants.rho) for c in contributions]), float(1)/Constants.rho)
        self.group_income = self.individual_share * Constants.players_per_group

        for p in self.get_players():
            contribution = p.contribution if p.contribution is not None else 0
            if self.subsession.round_number in self.session.vars['paying_round']:
                p.payoff = Constants.endowment - contribution + self.individual_share
            else:
                p.payoff = 0

            p.payoff_each_round = Constants.endowment - contribution + self.individual_share



class Player(BasePlayer):

    payoff_each_round = models.CurrencyField()
    contribution = models.CurrencyField(
        choices=list(range(0, Constants.endowment + 1)),
    )

    # Store calculator usage as JSON string for all submissions
    calculator_usage_log = models.LongStringField(blank=True)
