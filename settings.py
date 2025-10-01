from os import environ

# Modern oTree 5.x settings

# Admin credentials
ADMIN_USERNAME = 'yingzhi'
ADMIN_PASSWORD = '1015'

# Secret key - change this to something unique
SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'

# Debug mode
DEBUG = environ.get('OTREE_PRODUCTION') not in {None, '', '1'}

# Auth level
environ['OTREE_AUTH_LEVEL'] = 'STUDY'

# Currency settings
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

# Language
LANGUAGE_CODE = 'en-us'

# Points settings
POINTS_DECIMAL_PLACES = 2

# Demo page intro text
DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Below are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish to create your own variations.
    Click one to learn more and play.
</p>
"""

# Default session settings
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.125,
    participation_fee=0.00,
    num_bots=12,
    doc="",
)


SESSION_CONFIGS = [

    {
        'name': 'quiz_high_ten',
        'display_name': "quiz_high_ten",
        'num_demo_participants': 1,
        'app_sequence': ['quiz_high_ten','payment_info'],
                   },

    {
        'name': 'public_goods_high_ten',
        'display_name': "public_goods_high_ten",
        'num_demo_participants': 2,
        'app_sequence': ['quiz_high_ten','public_goods_high_ten','my_survey','payment_info'],
                   },

    {
        'name': 'quiz_high_four',
        'display_name': "quiz_high_four",
        'num_demo_participants': 1,
        'app_sequence': ['quiz_high_four','payment_info'],
                   },

    {
        'name': 'public_goods_high_four',
        'display_name': "public_goods_high_four",
        'num_demo_participants': 4,
        'app_sequence': ['quiz_high_four','public_goods_high_four','my_survey', 'payment_info'],
                   },

    {
        'name': 'quiz_low_ten',
        'display_name': "quiz_low_ten",
        'num_demo_participants': 1,
        'app_sequence': ['quiz_low_ten','payment_info'],
                   },

    {
        'name': 'public_goods_low_ten',
        'display_name': "public_goods_low_ten",
        'num_demo_participants': 10,
        'app_sequence': ['quiz_low_ten','public_goods_low_ten','my_survey','payment_info'],
                   },

    {
        'name': 'quiz_low_four',
        'display_name': "quiz_low_four",
        'num_demo_participants': 1,
        'app_sequence': ['quiz_low_four','payment_info'],
                   },
    {
        'name': 'my_survey',
        'display_name': "my_survey",
        'num_demo_participants': 1,
        'app_sequence': ['my_survey','payment_info'],
                   },

    {
        'name': 'public_goods_low_four',
        'display_name': "public_goods_low_four",
        'num_demo_participants': 4,
        'app_sequence': ['quiz_low_four', 'public_goods_low_four', 'my_survey', 'payment_info'],
                   },


]
ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'Behavioral_lab',
        'display_name': 'Behavioral lab I',
        'participant_label_file': 'lab.txt',
    },
]

# Modern oTree doesn't need augment_settings
