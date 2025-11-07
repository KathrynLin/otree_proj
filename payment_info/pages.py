from otree.api import *
# -*- coding: utf-8 -*-
import math
class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        payoff_so_far = self.player.participant.payoff
        true_payoff = payoff_so_far.to_real_world_currency(self.session)
        # Round up instead of round to 0: any amount larger than 1 but less than 2 will be rounded to 2
        # Round up all amounts > 0 (ceil), keep 0 as 0
        rounded_payoff = math.ceil(true_payoff) if true_payoff > 0 else 0
        total_earning = rounded_payoff + 5
        return {
            'redemption_code': participant.label or participant.code,
            'participant': participant,
            'payoff_so_far_money': rounded_payoff,
            'true_payoff': true_payoff,
            'total_earning': total_earning
        }


page_sequence = [PaymentInfo]
