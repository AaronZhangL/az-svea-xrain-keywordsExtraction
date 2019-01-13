#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_knowledgeManager.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang0@gamil.com>
#  

import sys
import svea_neo4jManager
import svea_wikipediaManager
import svea_analizeKeyWords

class svea_knowledgeManager(object):

  def __init__(self, _uriEnvString, _userEnvString, _passwordEnvString):
    print("***init class svea_knowledgeManager")
    self.neo4jMgr = svea_neo4jManager(_uriEnvString=_uriEnvString, 
                                      _userEnvString=_userEnvString, 
                                      _passwordEnvString=_passwordEnvString)
    self.wpMgr = svea_wikipediaManager()
    self.akwMgr = svea_analizeKeyWords()
  
  def createKnowledgeDBwithWikipediaPage(self,_wikipediaPageName):
    try:
      content = self.wpMgr.svea_getTextByPageName(_wikipediaPageName)
      doc = self.akdMgr.splitSentence(_modelType=akdMgr.modelTuple[0], _contentText=content)
      nounDic = self.akdMgr.getWordListOfSpecialWordType(_doc=doc, _wordType=akdMgr.POS_NOUN)

    except Exception as ex:
      print(ex)
      raise
    
def main(args):
    return 0

if __name__ == '__main__':
    kMgr = svea_knowledgeManager(_uriEnvString="NEO4J_URI", _userEnvString="NEO4J_USER", _passwordEnvString="NEO4J_PASSWORD")
    kmgr.createKnowledgeDBwithWikipediaPage("Customer-relationship_management")
    
    sys.exit(main(sys.argv))
