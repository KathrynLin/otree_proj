from otree.api import *


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return True


class Question(Page):
    def is_displayed(self):
        return True

    form_model = 'player'
    form_fields = ['question11','question12','question13',
    'question21','question22','question23','question31','question32','question33','question4','question5','question6']


class Feedback(Page):
    def is_displayed(self):
        return True

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    """Players payoff: How much each has earned"""
    def is_displayed(self):
        return True

    def vars_for_template(self):
        payoff_so_far = self.player.participant.payoff
        return {
                'payoff_so_far': payoff_so_far,
                'payoff_so_far_money': payoff_so_far.to_real_world_currency(self.session)
                }


page_sequence = [Introduction, Question, Feedback, Results]
