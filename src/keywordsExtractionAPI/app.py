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

def get_keywords_list(_modeType : str, _contentsText : str):
    """Get human-readable model name, language name and version."""
    keywords_list = ["abc","def","eee"]
    return keywords_list


#@hug.get('/keywordsList')
#def keywordsList():
#	keywordsList = keywords_list("debug","aaabbb")
#    return {"name" : "abc"}

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
    waitress.serve(__hug_wsgi__, port=9000)
    
