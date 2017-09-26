#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~
    Repository for application helpers.
"""

import os
import click
from flask.cli import FlaskGroup


def create_oxford_app(info):
    from oxford import create_app
    return create_app(
        config_filename=os.environ.get('OXFORD_CONFIG_FILENAME', 'config.py'))


@click.group(cls=FlaskGroup, create_app=create_oxford_app)
def cli():
    """The Oxford dictionary Restful API."""


@cli.command()
@click.option('--source', help='the dictionary source file')
@click.confirmation_option(help='Are you sure you want to replace a db?')
def load(source=""):
    """Load the DB with the source file"""
    from oxford.dictionary import Dictionary
    from oxford.models import db

    db.drop_all()
    db.create_all()

    with open(source, 'r') as f:
        Dictionary.load([
            line.strip().decode('utf-8')
            for line in f
            if line.strip()
        ])

    click.echo('Data loading complete')
    return


if __name__ == '__main__':
    cli()
