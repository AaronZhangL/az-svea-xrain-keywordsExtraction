#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_knowledgeManager.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang0@gamil.com>
#  

import sys
from svea_neo4jManager import svea_neo4jManager
from svea_wikipediaManager import svea_wikipediaManager
from svea_analizeKeyWords import svea_analizeKeyWords

class svea_knowledgeManager(object):

  def __init__(self, _uriEnvStr, _userEnvStr, _passwordEnvStr):
    print("***init class svea_knowledgeManager")
    self.neo4jMgr = svea_neo4jManager(_uriEnvString=_uriEnvStr, _userEnvString=_userEnvStr, _passwordEnvString=_passwordEnvStr)
    self.wpdMgr = svea_wikipediaManager()
    self.akwMgr = svea_analizeKeyWords()
  
  def createKnowledgeDBwithWikipediaPage(self,_wikipediaPageName):
    try:
      # get wikipedia page instance
      objWpp = self.wpdMgr.svea_getTextByPageName(_wikipediaPageName)
      
      # get NOUN words list
      doc = self.akwMgr.splitSentence(_modelType=self.akwMgr.modelTuple[0], _contentText=objWpp.page.content)
      
      # get words pos dictionary
      nounDic = self.akwMgr.getWordListOfSpecialWordType(_doc=doc, _wordType=self.akwMgr.POS_NOUN)
      
      # Add titile node dictionary to neo4j
      print("-------------------------------------------------------")
      print("Add titile node dictionary to neo4j")
      print("-------------------------------------------------------")
      titleNode = {objWpp.page.title:[objWpp.page.title, "NOUN", "-"]}
      titleNodeList = self.neo4jMgr.addWordNode(titleNode)
      
      # Add words dictionary to neo4j
      print("-------------------------------------------------------")
      print("Add words dictionary to neo4j")
      print("-------------------------------------------------------")
      nodeList = self.neo4jMgr.addWordNode(nounDic)
      
      # Create relationship between title node and normal word node
      print("-------------------------------------------------------")
      print("Create relationship between title node and normal word node")
      print("-------------------------------------------------------")
      for key, value in nounDic.items():
        relationshipTypeList = self.neo4jMgr.createRelationship(titleNode[objWpp.page.title], value)
        print(titleNode)
        print(value)
        print(relationshipTypeList)
      print("***node list***")
      print(nodeList)
      
    except Exception as ex:
      print(ex)
      raise
    
def main(args):
    return 0

if __name__ == '__main__':
    kMgr = svea_knowledgeManager(_uriEnvStr="NEO4J_URI", _userEnvStr="NEO4J_USER", _passwordEnvStr="NEO4J_PASSWORD")
    kMgr.createKnowledgeDBwithWikipediaPage("Customer-relationship_management")
    
    sys.exit(main(sys.argv))
