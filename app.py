# things.py

import falcon
import json
from db import DB

class PagesResource(object):
  # Handles GET requests
  def on_get(self, req, resp):
    resp.status = falcon.HTTP_200
    resp.body = db.get_pages()

  # handle POST requests
  def on_post(self, req, resp):
    post = req.stream.read()
    try:
      json_data = json.loads(post)
    # Not valid data

    except ValueError as e:
      resp.status = falcon.HTTP_400
      resp.body = json.dumps('Error decoding JSON')

    else:
      # Check if data contain 'title' and 'url' keys
      if 'title' not in json_data or 'url' not in json_data:
        resp.status = falcon.HTTP_400
        resp.body = json.dumps('Error decoding JSON')
      else:
        # Add page to db
        db.add_page(json_data)
        resp.status = falcon.HTTP_200


api = falcon.API()

# Load database
db = DB()

api.add_route('/pages', PagesResource())