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

# python -m spacy download en
class KeyWords:
  modelTuple = ("en", "en_core_web_sm")
  
  def __init__(self):
    print("***AZ[Init KeyWords class]")

  def splitSentenceEn(self):
    nlp = spacy.load(self.modelTuple[0])
    doc = nlp(u"This is a sentence.")
    print([(w.text, w.pos_) for w in doc])

  def splitSentenceEnCoreWebSm(self):
    nlp = spacy.load(self.modelTuple[1])
    doc = nlp(sentences[0])
    print(doc.text)
    for token in doc:
      print(token.text, token.pos_, token.dep_)
    
  # python -m spacy download en_core_web_sm
  def splitSentence(self, _modelType):
    if _modelType == self.modelTuple[0]:
      self.splitSentenceEn()
    elif _modelType == self.modelTuple[1]:
      self.splitSentenceEnCoreWebSm()
    else:
      print("No model be choosed!")

def main(args):
    return 0

if __name__ == '__main__':
    kw = KeyWords()
    kw.splitSentence(_modelType=kw.modelTuple[1])
    #sys.exit(main(sys.argv))
