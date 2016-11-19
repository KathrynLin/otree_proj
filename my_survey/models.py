# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import otree.settings
import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

from django_countries.fields import CountryField
from django import forms

author = 'Yingzhi Liang'

doc = """
Standard Demographic Survey from Veconlab
"""




class Constants(BaseConstants):
    name_in_url = 'my_survey'
    players_per_group = None
    num_rounds = 1
    lottery_safe_A = c(2.00)
    lottery_safe_B = c(1.60)
    lottery_risk_A = c(3.85)
    lottery_risk_B = c(0.10)



class Subsession(BaseSubsession):
    paying_choice = random.randint(1, 10)
    die = random.randint(1,10)




class Group(BaseGroup):
    pass


class Player(BasePlayer):


    q_instruction1 = models.CharField(initial=None,blank=True,
                                    verbose_name='Which part of the instruction is unclear for you?')
    q_instruction2 = models.CharField(initial=None,blank=True,
                                    verbose_name='What can we do to make it clear?')
    q_instruction3 = models.CharField(initial=None,blank=True,
                                    verbose_name='Any suggestions for this experiment?')
    q_instruction4 = models.CharField(initial=None,blank=True,
                                    verbose_name='Any questions about this experiment?')
    q_country = CountryField(blank=True,verbose_name='What is your country of citizenship?')
    q_age = models.PositiveIntegerField(verbose_name='What is your age?',blank=True,
                                        choices=range(13, 125),
                                        initial=None)
    q_gender = models.CharField(initial=None,blank=True,
                                choices=['Male', 'Female'],
                                verbose_name='What is your gender?',
                                widget=widgets.RadioSelect())
    q_ethnic = models.CharField(initial=None,blank=True,
                                verbose_name='Which of the following best describes your racial or ethnic background?',
                                choices=['Asian', 'Black', 'Hispanic', 'Multi-racial', 'Native-American', 'Caucasion'])
    q_marriage = models.CharField(initial=None,blank=True,verbose_name='What is your marital status?',
                                choices=['Never Married', 'Currently Married', 'Previously Married'])
    q_employ = models.CharField(initial=None,blank=True,verbose_name='How would you best describe your employment status?',
                                choices=['Employed, Full Time', 'Employed, Part Time', 'Not Employed'])
    q_student = models.CharField(initial=None,blank=True,verbose_name='What is your student status?',
                                choices=['Full Time', 'Part Time (less than the normal full-course load)', 'Non Student'])
    q_education = models.CharField(initial=None,blank=True,verbose_name='What is the highest level of study that you have completed?(Use your current year in school if you are a student.)',
                                choices=['College Freshman (first-year)', 'College Sophomore (second-year)', 'College Junior (third-year)',
                                'College Senior (fourth-year)', 'Graduate (first-year)', 'Graduate (second-year)', 'Graduate (third-year)',
                                'Graduate (4+ years)'])
    q_major = models.CharField(initial=None,blank=True,verbose_name='Which of the following best describes your current major course of study?)',
                                choices=['No Major or Pre-College', 'Arts/Humanities/Education', 'Business/Management (including MBA)',
                                'Economics', 'Politics', 'Psychology', 'Other Social Science', 'Law School (but not pre-law)',
                                'Medical/Nursing (but not pre-med)', 'Math/Science/Engineering/Computer Science', 'Other']
                                )
    q_siblings = models.CharField(initial=None,blank=True,verbose_name='How many brothers and sisters do you have? (Please do not count yourself.)',
                                choices=['no others', '1 other', '2 others', '3 others', '4 others', '5 others', '6 or more others'])
    q_vote = models.CharField(initial=None,blank=True,
                              choices=['Yes', 'No'],
                              verbose_name='Have you ever voted in a state or federal government election (in any country)?',
                              widget=widgets.RadioSelect())
    q_job = models.CharField(initial=None,blank=True,verbose_name='What is the most appropriate description of your primary employment (if any)?',
                               choices=['Not Employed/Student(without outside employment)', 'Agriculture', 'Business/Management', 'Clerical',
                               'Manufacturing', 'Government (non-military)', 'homemaker', 'Military', 'Professional (Law, Medicine, Architecture)',
                               'Research or Research Assistant', 'Teaching or Teaching Assistant', 'Waitperson/Food Service', 'Other'])
    q_income = models.CharField(initial=None,blank=True,verbose_name='Which category best corresponds to the combined income for all members of your household?(Please guess if you are not sure.)',
                               choices=['Below $10,000', '$10,001 - $20,000', '$20,001 - $30,000', '$30,001 - $40,000',
                               '$40,001 - $50,000', '$50,001 - $60,000', '$60,001 - $70,000', '$70,001 - $80,000',
                               '$80,001 - $90,000', '$90,001 - $100,000', '$100,001 - $120,000', '$120,001 - $140,000',
                               '$140,001 - $160,000', '$160,001 - $180,000', '$180,001 - $200,000', 'above $200,000'])
    q_lottery1 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery2 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery3 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery4 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery5 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery6 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery7 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery8 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery9 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery10 = models.CharField(verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery_instruction1 = models.CharField(initial=None, blank=True, verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery_instruction2 = models.CharField(initial=None, blank=True, verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery_instruction3 = models.CharField(initial=None, blank=True, verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    q_lottery_instruction4 = models.CharField(initial=None, blank=True, verbose_name='', choices=['A', 'B'],
                                widget=widgets.RadioSelectHorizontal())
    def choice_list(self):
        self.choice = [self.q_lottery1, self.q_lottery2, self.q_lottery3, self.q_lottery4, self.q_lottery5, self.q_lottery6, self.q_lottery7, self.q_lottery8, self.q_lottery9, self.q_lottery10]
        return self.choice

    def set_payoff(self):
        exchange_rate = self.session.config['real_world_currency_per_point']
        if self.choice_list()[Subsession.paying_choice] == 'A':
            if Subsession.die < Subsession.paying_choice + 1:
                self.payoff = Constants.lottery_safe_A /exchange_rate
            else:
                self.payoff = Constants.lottery_safe_B /exchange_rate
        else:
            if Subsession.die < Subsession.paying_choice + 1:
                self.payoff = Constants.lottery_risk_A /exchange_rate
            else:
                self.payoff = Constants.lottery_risk_B /exchange_rate
