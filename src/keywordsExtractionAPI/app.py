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
    
MODELS = {
    'en_core_web_sm': spacy.load('en_core_web_sm'),
    'en_core_web_md': spacy.load('en_core_web_md'),
    'en_core_web_lg': spacy.load('en_core_web_lg')
}

def get_model_desc(nlp, model_name):
    """Get human-readable model name, language name and version."""
    lang_cls = spacy.util.get_lang_class(nlp.lang)
    lang_name = lang_cls.__name__
    model_version = nlp.meta['version']
    return '{} - {} (v{})'.format(lang_name, model_name, model_version)


@hug.get('/models')
def models():
    return {name: get_model_desc(nlp, name) for name, nlp in MODELS.items()}


@hug.post('/dep')
def dep(text: str, model: str, collapse_punctuation: bool=False,
        collapse_phrases: bool=False):
    """Get dependencies for displaCy visualizer."""
    nlp = MODELS[model]
    doc = nlp(text)
    if collapse_phrases:
        for np in list(doc.noun_chunks):
            np.merge(tag=np.root.tag_, lemma=np.root.lemma_,
                     ent_type=np.root.ent_type_)
    options = {'collapse_punct': collapse_punctuation}
    return spacy.displacy.parse_deps(doc, options)


@hug.post('/ent')
def ent(text: str, model: str):
    """Get entities for displaCy ENT visualizer."""
    nlp = MODELS[model]
    doc = nlp(text)
    return [{'start': ent.start_char, 'end': ent.end_char, 'label': ent.label_}
            for ent in doc.ents]

if __name__ == '__main__':

    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))
    waitress.serve(__hug_wsgi__, port=8080)
    
