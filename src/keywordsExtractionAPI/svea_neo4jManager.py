#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_neo4jManager.py
#  
#  Copyright 2019 Aaron Zhang <aaronzhang0@gmail.com>
#  

import sys, os
from neo4j import GraphDatabase

#
# Port List:
# 7474 for HTTP.
# 7473 for HTTPS.
# 7687 for Bolt.
#

class svea_neo4jManager(object):

  def __init__(self, _uriEnvString, _userEnvString, _passwordEnvString):
    uri = os.getenv(_uriEnvString)
    user = os.getenv(_userEnvString)
    password = os.getenv(_passwordEnvString)
    self._driver = GraphDatabase.driver(uri, auth=(user, password), connection_timeout=15)

  def close(self):
    self._driver.close()

  def print_greeting(self, message):
    with self._driver.session() as session:
      greeting = session.write_transaction(self._create_and_return_greeting, message)
      
  @staticmethod
  def _create_and_return_greeting(tx, message):
    result = tx.run("CREATE (a:Greeting) "
                    "SET a.message = $message "
                    "RETURN a.message + ', from node ' + id(a)", message=message)
    return result.single()[0]
    
  def print_friends_of(self, tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.name", name=name):
      print(record["f.name"])

#def main(args):
#    return 0

if __name__ == '__main__':
  n4Mgr = svea_neo4jManager(_uriEnvString="NEO4J_URI", _userEnvString="NEO4J_USER", _passwordEnvString="NEO4J_PASSWORD")
  with n4Mgr._driver.session() as session:
    session.write_transaction(n4Mgr._create_and_return_greeting, "aaron")
  print("***main")
  #sys.exit(main(sys.argv))
