# db.py
from pymongo import MongoClient
from bson.json_util import dumps

class DB(object):
  db = None

  def __init__(self):
    c = MongoClient()
    self.db = c.peregrin

  def get_pages(self):
    resp = self.db.pages.find({}, {'url': 1, 'title': 1, '_id': 0})
    return dumps(resp)

  def add_page(self, page):
    self.db.pages.insert(page)