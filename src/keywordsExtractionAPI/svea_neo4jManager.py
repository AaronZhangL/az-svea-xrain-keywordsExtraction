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

  def read_all(self):
    """Read all record.

    Args:
      NONE
    Raises:
      OSError: If call some OS level lib failed.
      ValueError: If the minimum port specified is less than 1024.
    Returns:
      The result of search Neo4J database.
    """
    try:
      with self._driver.session() as session:
        result = session.run("MATCH (n) RETURN n")
        records = list(result)
        print(len(records))
        for record in records:
          print(record["n"])
        return result
    except OSError as err:
      print("OS error: {0}".format(err))
    except ValueError:
      print("Cannot get some value!")
    except Exception as ex:
      print(ex)
      raise

  def addWordNode(self, _wordNodes):
    """Add words dictionary to neo4j

    Args:
      Words dictionary, format=> {'noun-word': ['noun-word', 'NOUN', 'dobj']}
    Raises:
      xxx: xxxxxxxxxxxxx
    Returns:
      Words list return from neo4j
    """
    returnList = []
    with self._driver.session() as session:
      for key, value in _wordNodes.items():
        wordNode = session.write_transaction(self._createAndReturnWordNode, value)
        print(wordNode)
        returnList.append(wordNode)
    return returnList

  @staticmethod
  def _createAndReturnWordNode(tx, _wordNode):
    result = tx.run("CREATE (a:Word) "
                    "SET a.text = $_text, "
                    "a.pos = $_pos, "
                    "a.dep = $_dep "
                    "RETURN a", _text=_wordNode[0], _pos=_wordNode[1], _dep=_wordNode[2])
    return result.single()[0]

  def createRelationship(self, _titleNode, _wordNode):
    """Create relationship between title node and word nodes.

    Args:
      Title words dictionary, format=> {'noun-word': ['noun-word', 'NOUN', 'dobj']}
      Words dictionary, format=> {'noun-word': ['noun-word', 'NOUN', 'dobj']}
    Raises:
      xxx: xxxxxxxxxxxxx
    Returns:
      Words list return from neo4j, format => [<Node id=1992 labels={'Word'} properties={'pos': 'NOUN', 'text': 'References', 'dep': 'dobj'}>]
    """
    returnList = []
    print(_titleNode, _wordNode)
    with self._driver.session() as session:
      relationshipType = session.write_transaction(self._createAndReturnWordNodeWithRelationship, _titleNode, _wordNode)
      print(relationshipType)
      returnList.append(relationshipType)
    return returnList
    
  @staticmethod
  def _createAndReturnWordNodeWithRelationship(tx, _titleNode, _wordNode):
    #{'References': ['References', 'NOUN', 'dobj']}
    result = tx.run("MATCH (a:Word),(b:Word) "
                    "WHERE a.text = $_worldNode AND "
                    "b.text = $_titleNode "
                    "CREATE (a)-[r:WIKIPEDIA_IN]->(b)"
                    "RETURN type(r)", _worldNode=_wordNode[0], _titleNode=_titleNode[0])
    return result
    
def main(args):
  return 0

if __name__ == '__main__':
  n4Mgr = svea_neo4jManager(_uriEnvString="NEO4J_URI", _userEnvString="NEO4J_USER", _passwordEnvString="NEO4J_PASSWORD")
  result = n4Mgr.read_all()
    
  print("***main")
  sys.exit(main(sys.argv))
