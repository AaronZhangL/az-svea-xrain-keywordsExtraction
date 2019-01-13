#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_analizeKeyWords.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang@localhost.localhostdomain>
#  

import sys
import spacy
from spacy.lang.en.examples import sentences
from svea_wikipediaManager import svea_wikipediaManager

class svea_analizeKeyWords(object):
  modelTuple = ("en", "en_core_web_sm")
  
  # POS words type list
  POS_NOUN = "NOUN"
  
  def __init__(self):
    print("***AZ[Init KeyWords class]")
    
  # python -m spacy download en
  def splitSentenceEn(self, _contentText):
    nlp = spacy.load(self.modelTuple[0])
    #doc = nlp(u"This is a sentence.")
    doc = nlp(_contentText)
    print([(w.text, w.pos_) for w in doc])
    return doc

  def splitSentenceEnCoreWebSm(self, _contentText):
    nlp = spacy.load(self.modelTuple[1])
    doc = nlp(_contentText)
    #print(doc.text)
    for token in doc:
      print(token.text, token.pos_, token.dep_)
    return doc

  # Get word list by special word type
  # POS: https://spacy.io/api/annotation
  def getWordListOfSpecialWordType(self, _doc, _wordType):
    _nounDic = {}
    for token in _doc:
      #print(token.text, token.pos_, token.dep_)
      if (token.pos_ == "NOUN"):
        _nounDic[token.text] = [token.text, token.pos_, token.dep_]
    return _nounDic

  # python -m spacy download en_core_web_sm
  def splitSentence(self, _modelType, _contentText):
    doc = ""
    if _modelType == self.modelTuple[0]:
      doc = self.splitSentenceEn(_contentText)
    elif _modelType == self.modelTuple[1]:
      _contentText = sentences[0]
      doc = self.splitSentenceEnCoreWebSm(_contentText)
    else:
      print("No model be choosed!")
    return doc

  # Analize file contents
  def splitSentenceFromFile(self, _modelType, _textFile):
    file = open(_textFile, "r")
    _contentText = file.read()
    doc = self.splitSentence(_modelType, _contentText)
    return doc
    

def main(args):
    return 0

if __name__ == '__main__':
    # get text
    wpMgr = svea_wikipediaManager()
    content = wpMgr.svea_getTextByPageName("Customer-relationship_management")
    akdMgr = svea_analizeKeyWords()
    
    # test 1
    #akdMgr.splitSentence(_modelType=akdMgr.modelTuple[1])
    
    # test 2 intergrate wikpedia
    #doc = akdMgr.splitSentence(_modelType=akdMgr.modelTuple[0], _contentText=content)
    
    # test 3 test file content
    doc = akdMgr.splitSentenceFromFile(_modelType=akdMgr.modelTuple[0], _textFile="../../testData/textData1.txt")
    
    # test 4: test word POS
    nounDic = akdMgr.getWordListOfSpecialWordType(_doc=doc, _wordType=akdMgr.POS_NOUN)
    print("=======================================")
    print(nounDic)
    
    sys.exit(main(sys.argv))
