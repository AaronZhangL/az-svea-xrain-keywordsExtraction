#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_wikipediaManager.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang0@gmail.com>
#  

#pip install wikipedia
import sys
import wikipedia
from svea_ObjWikipediaPage import svea_ObjWikipediaPage

class svea_wikipediaManager(object):
  
  def __init__(self):
    print("***AZ[Init svea_wikipediaManager class]")

  def svea_getTextByPageName(self, _pageName):
    objWpp = svea_ObjWikipediaPage(_pageName)
    objWpp.page = wikipedia.page(_pageName)
    #print("***page type: " + str(type(page)) )
    print(objWpp.page.url)
    print(objWpp.page.title)
    #content = objWpp.page.content # Content of page.
    return objWpp
    
def main(args):
    return 0

if __name__ == '__main__':
    wpMgr = svea_wikipediaManager()
    objWpp = wpMgr.svea_getTextByPageName("Customer-relationship_management")
    content = objWpp.page.content
    title = objWpp.page.title
    url = objWpp.page.url
    print("***main function")
    print(url)
    print(title)
    print(content)
    
    #sys.exit(main(sys.argv))
