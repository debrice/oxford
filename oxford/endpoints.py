# -*- coding: utf-8 -*-
"""
    endpoints
    ~~~~~~~~~
    The Oxford dictionary Rest endpoints.
"""
from flask import request
from flask_restful import Resource, abort
from oxford.dictionary import Dictionary


class OxfordDictionaryAPI(Resource):
    def get(self):
        word = request.args.get('word', '').strip().lower()

        # word argument on the query string is required
        if not word:
            abort(400, message="the argument \"word\" is required")

        match = Dictionary.search(word)

        if match:
            return match
        else:
            abort(404, message="word \"%s\" not found" % word)
