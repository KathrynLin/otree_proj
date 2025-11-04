from otree.api import *
# <standard imports>

import random

# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_low_ten'
    players_per_group = None
    num_rounds = 1
    point_per_correct = 1.6
    endowment = 10
    # correct answer for pre-test
    question11_correct = 72.67
    question12_correct = 9
    question13_correct = 81.67
    question21_correct = 78.41
    question22_correct = 5
    question23_correct = 83.41
    question31_correct = 83.83
    question32_correct = 0
    question33_correct = 83.83
    question4_correct = 5
    question5_correct = 5
    question6_correct = 5


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question11 = models.CurrencyField(decimal_places=2)
    question12 = models.CurrencyField(decimal_places=2)
    question13 = models.CurrencyField(decimal_places=2)
    question21 = models.CurrencyField(decimal_places=2)
    question22 = models.CurrencyField(decimal_places=2)
    question23 = models.CurrencyField(decimal_places=2)
    question31 = models.CurrencyField(decimal_places=2)
    question32 = models.CurrencyField(decimal_places=2)
    question33 = models.CurrencyField(decimal_places=2)
    question4 = models.CurrencyField(
        choices=list(range(0, Constants.endowment + 1)),
    )
    question5 = models.CurrencyField(
        choices=list(range(0, Constants.endowment + 1)),
    )
    question6 = models.CurrencyField(
        choices=list(range(0, Constants.endowment + 1)),
    )

    num_correct_questions = models.IntegerField(initial=0)

    # Calculator usage per page - JSON array of calculator submissions
    # Format: [{member1, member2, member3, my, timestamp, url}, ...]
    calc_introduction = models.LongStringField(blank=True, initial='[]')
    calc_question = models.LongStringField(blank=True, initial='[]')
    calc_feedback = models.LongStringField(blank=True, initial='[]')

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
