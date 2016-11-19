# -*- coding: utf-8 -*-
from __future__ import division
import math
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        payoff_so_far = self.player.participant.payoff
        return {
            'redemption_code': participant.label or participant.code,
            'participant': participant,
            'payoff_so_far_money': round(payoff_so_far.to_real_world_currency(self.session))
        }


page_sequence = [PaymentInfo]
