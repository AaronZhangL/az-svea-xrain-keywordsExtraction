#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#
#  Copyright 2019 Aaron Zhang <aaronzhang0@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from __future__ import unicode_literals

import hug
from hug_middleware_cors import CORSMiddleware
import spacy
import waitress

"""A simple post reading server example.
To test run this server with `hug -f post_body_example`
then run the following from ipython:
    import requests
    requests.post('http://localhost:8000/post_here', json={'one': 'two'}).json()
    This should return back the json data that you posted
"""
@hug.post()
def post_here(body):
    """This example shows how to read in post data w/ hug outside of its automatic param parsing"""
    name = body["name"] + " Zhang"
    age = body["age"] + 1
    return {"full-name":[name], "real age":age}

# Test: http://localhost:9000/keywordsList?content=abcd
# return: "aaron - abcd!"
@hug.get('/keywordsList')
def keywordsList(content: str):
    newstr = "MongoDB Record ID is"
    return "{newstr} - [{content}]".format(**locals())

@hug.get('/questionKey')
def keywordsList(recordID: str):
    newstr = "MongoDB Record ID is"
    return "{newstr} - {content}".format(**locals())

# Test: http://localhost:9000/greet/wishes
@hug.get('/greet/{event}')
def greet(event: str):
    """Greets appropriately (from http://blog.ketchum.com/how-to-write-10-common-holiday-greetings/)  """
    greetings = "Happy"
    if event == "Christmas":
        greetings = "Merry"
    if event == "Kwanzaa":
        greetings = "Joyous"
    if event == "wishes":
        greetings = "Warm"

    return "{greetings} {event}!".format(**locals())


if __name__ == '__main__':
    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))
    waitress.serve(__hug_wsgi__, host='0.0.0.0', port=9000)
    # How to start this service => $ phthon app.py
