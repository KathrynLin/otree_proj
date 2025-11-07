# -*- coding: utf-8 -*-
from otree.api import Page, WaitPage
from .models import Constants


class Contribute(Page):

    """Player: Choose how much to contribute"""

    form_model = "player"
    form_fields = ['contribution', 'calc_contribute']

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

    form_model = "player"
    form_fields = ['calc_results']

    def vars_for_template(self):

        return {
            'total_group_income': self.group.group_income,
            'earnings_from_private': Constants.endowment - self.player.contribution,
            'earnings_from_public': self.group.individual_share,
            'individual_earnings': self.player.payoff_each_round,
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'player_in_all_rounds': self.player.in_all_rounds()
        }


class FinalResult(Page):

    form_model = "player"
    form_fields = []

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def live_method(self, data):
        # Receive calculator data from JavaScript
        if 'calculator_data' in data:
            self.participant.vars['calculator_data'] = data['calculator_data']

    def before_next_page(self):
        # Save ALL accumulated calculator data to the quiz player's calculator_usage_log_all field
        calculator_data = self.participant.vars.get('calculator_data', '[]')

        # Find the quiz player for this participant
        quiz_player = getattr(self.participant, 'quiz_low_ten_player', None)
        if quiz_player and calculator_data:
            # Save all accumulated data (quiz + game rounds) to the new field
            quiz_player.calculator_usage_log_all = calculator_data

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        total_payoff = sum([p.payoff for p in player_in_all_rounds])
        paying_round = self.session.vars['paying_round']
        payoff_so_far = self.player.participant.payoff
        payoff_so_far_money = payoff_so_far.to_real_world_currency(self.session)
        total_earning_with_fee = payoff_so_far_money + 5


        return {'player_in_all_rounds': player_in_all_rounds,
                'total_payoff': total_payoff,
                'paying_round': paying_round,
                'payoff_so_far': payoff_so_far,
                'payoff_so_far_money': payoff_so_far_money,
                'total_earning_with_fee': total_earning_with_fee
                }

# page_sequence = [Introduction,
#             Question,
#             Feedback,
#             Contribute,
#             ResultsWaitPage,
#             Results,
#             FinalResult]
page_sequence = [Contribute, ResultsWaitPage, Results, FinalResult]
