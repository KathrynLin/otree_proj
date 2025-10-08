from otree.api import *
# -*- coding: utf-8 -*-
import math
class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        payoff_so_far = self.player.participant.payoff
        true_payoff = payoff_so_far.to_real_world_currency(self.session)
        return {
            'redemption_code': participant.label or participant.code,
            'participant': participant,
            'payoff_so_far_money': round(true_payoff),
            'true_payoff': true_payoff
        }


page_sequence = [PaymentInfo]
