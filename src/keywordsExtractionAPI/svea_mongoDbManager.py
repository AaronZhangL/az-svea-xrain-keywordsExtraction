#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svea_mongoDbManager.py
#
#  Copyright 2019 Aaron Zhang <aaronzhang0@gmail.com>
#

import sys, os
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

#
# Port List:
#

# See: http://api.mongodb.com/python/current/tutorial.html
class svea_mongoDbManager(object):

  def __init__(self, _uriEnvString, _userEnvString, _passwordEnvString):
    uri = os.getenv(_uriEnvString) #uri='mongodb://localhost:27017/'
    user = os.getenv(_userEnvString)
    password = os.getenv(_passwordEnvString)
    self._client = MongoClient(uri)
    self._database = self._client["crud"]
    self._collection = self._database["characters"]

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
        print("TODO")

    except OSError as err:
      print("OS error: {0}".format(err))
    except ValueError:
      print("Cannot get some value!")
    except Exception as ex:
      print(ex)
      raise

  # The web framework gets post_id from the URL and passes it as a string
  def get(self, postId):
    return ObjectId(postId)

  def selectByID(self, mongoDbID):
    try:
      # Convert from string to ObjectId:
      mongoDbIDObj = self.get(mongoDbID)
      document = self._collection.find_one({'_id': mongoDbIDObj})
      return document
    except Exception as ex:
      print(ex)
      raise

def main(args):
  return 0

if __name__ == '__main__':
  # export MONGODB_URI="mongodb://localhost:27017/"
  # export MONGODB_USER="NONE"
  # export MONGODB_PASSWORD="NONE"
  mdbMgr = svea_mongoDbManager(_uriEnvString="MONGODB_URI", _userEnvString="MONGODB_USER", _passwordEnvString="MONGODB_PASSWORD")
  result = mdbMgr.selectByID(mongoDbID="5c41418c01192e2a003fee29")
  print(result)
  print("***main")
  sys.exit(main(sys.argv))
