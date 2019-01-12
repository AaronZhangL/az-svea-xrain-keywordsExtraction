#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_wikipediaManager.py
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

#pip install wikipedia
import sys
import wikipedia

class svea_wikipediaManager:
  
  def __init__(self):
    print("***AZ[Init svea_wikipediaManager class]")

  def svea_getTextByPageName(self, _pageName):
    page = wikipedia.page(_pageName)
    print(page.url)
    print(page.title)
    content = page.content # Content of page.
    #print(content)
    return content
    
def main(args):
    return 0

if __name__ == '__main__':
    wpMgr = svea_wikipediaManager()
    wpMgr.svea_getTextByPageName("Customer-relationship_management")
    
    #sys.exit(main(sys.argv))
