# -*- coding: utf-8 -*-
"""
    test_config
    ~~~~~~~~~~~
    This is the config used for testing see the oxford/config.py
    for production config
"""
from oxford.config import *


# Database in memory for testing
SQLALCHEMY_DATABASE_URI = 'sqlite://'
