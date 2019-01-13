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

class svea_wikipediaManager(object):
  
  def __init__(self):
    print("***AZ[Init svea_wikipediaManager class]")

  def svea_getTextByPageName(self, _pageName):
    page = wikipedia.page(_pageName)
    print(page.url)
    print(page.title)
    content = page.content # Content of page.
    return content
    
def main(args):
    return 0

if __name__ == '__main__':
    wpMgr = svea_wikipediaManager()
    content = wpMgr.svea_getTextByPageName("Customer-relationship_management")
    print(content)
    
    #sys.exit(main(sys.argv))
