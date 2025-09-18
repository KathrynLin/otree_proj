from otree.api import *

import random
import math


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


source_code = ""


bibliography = ()


links = {}


keywords = ()


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.payoff = 0



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass
