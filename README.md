# oTree Project

**Note: This project has been updated from oTree 1.x (circa 2016) to work with modern oTree 5.x**

## Live demo
http://demo.otree.org/

## Homepage
http://www.otree.org/

## About

oTree is a framework for implementing multiplayer decision strategy games and experiments.
Many of the details of writing a web application are abstracted away,
meaning that the code is focused on the logic of the game.
oTree programming is accessible to programmers without advanced experience in web app development.

This repository contains various experimental games including:
- Public goods games (with different group sizes and parameters)
- Quiz applications for comprehension tests
- Survey applications for demographic data collection
- Payment information modules

## Quick start

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Installation and Setup

1. **Create and activate virtual environment** (if not already done):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements_base.txt
```

3. **Initialize database**:
```bash
otree resetdb --noinput
```

4. **Start development server**:
```bash
otree devserver
```

The server will start and display a URL (typically http://localhost:8000) where you can access the experiments.

## Available Experiments

This project includes several experimental sessions:

- **quiz_high_ten**: Comprehension quiz for high-parameter 10-player treatment
- **public_goods_high_ten**: Public goods game with 10 players and high parameters
- **quiz_high_four**: Comprehension quiz for high-parameter 4-player treatment
- **public_goods_high_four**: Public goods game with 4 players and high parameters
- **quiz_low_ten**: Comprehension quiz for low-parameter 10-player treatment
- **public_goods_low_ten**: Public goods game with 10 players and low parameters
- **quiz_low_four**: Comprehension quiz for low-parameter 4-player treatment
- **public_goods_low_four**: Public goods game with 4 players and low parameters
- **my_survey**: Demographic and preference survey

## Migration Notes

This project was originally built with oTree 1.x and has been updated to work with oTree 5.x. Key changes made:

- Updated package dependencies from legacy versions to modern oTree 5.x
- Converted model imports from `otree.db` to `otree.api`
- Updated class naming from `Constants` to `C`
- Fixed currency field syntax and choices
- Updated session lifecycle methods (`before_session_starts` → `creating_session`)
- Removed Django-specific dependencies not needed in modern oTree

## Contact
chris@otree.org (you can also add me on Skype by searching this email address; please mention oTree in your contact request)

**Please contact me if any part of oTree does not work for you (or is unclear).**

## Contributors

* Juan B. Cabral (http://jbcabral.org/, https://github.com/leliel12)
* Gregor Muellegger (http://gremu.net/, https://github.com/gregmuellegger)
* Alexander Schepanovski (https://github.com/Suor/)
* Alexander Sandukovskiy
* Som Datye

## Mailing list
[Help & discussion mailing list](https://groups.google.com/forum/#!forum/otree)

# Docs

http://otree.readthedocs.org

# Status

![RTD Badge](https://readthedocs.org/projects/otree/badge/?version=latest)
