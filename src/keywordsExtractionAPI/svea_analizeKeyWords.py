#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_analizeKeyWords.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang@localhost.localhostdomain>
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

import sys
import spacy
from spacy.lang.en.examples import sentences
from svea_wikipediaManager import svea_wikipediaManager

class KeyWords:
  modelTuple = ("en", "en_core_web_sm")
  
  def __init__(self):
    print("***AZ[Init KeyWords class]")
    
  # python -m spacy download en
  def splitSentenceEn(self, _contentText):
    nlp = spacy.load(self.modelTuple[0])
    #doc = nlp(u"This is a sentence.")
    doc = nlp(_contentText)
    print([(w.text, w.pos_) for w in doc])

  def splitSentenceEnCoreWebSm(self, _contentText):
    nlp = spacy.load(self.modelTuple[1])
    doc = nlp(_contentText)
    print(doc.text)
    for token in doc:
      print(token.text, token.pos_, token.dep_)
    
  # python -m spacy download en_core_web_sm
  def splitSentence(self, _modelType, _contentText):
    if _modelType == self.modelTuple[0]:
      self.splitSentenceEn(_contentText)
    elif _modelType == self.modelTuple[1]:
      _contentText = sentences[0]
      self.splitSentenceEnCoreWebSm(_contentText)
    else:
      print("No model be choosed!")

def main(args):
    return 0

if __name__ == '__main__':
    # get text
    wpMgr = svea_wikipediaManager()
    content = wpMgr.svea_getTextByPageName("Customer-relationship_management")
    kw = KeyWords()
    
    # test 1
    #kw.splitSentence(_modelType=kw.modelTuple[1])
    
    # test 2 intergrate wikpedia
    kw.splitSentence(_modelType=kw.modelTuple[0], _contentText=content)
    
    
    #sys.exit(main(sys.argv))
