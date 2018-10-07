#!/usr/bin/env python
import cgi
import logging
import models
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

redirect_key = ndb.Key('Go Redirector', 'default_redirector')

class GoLink(webapp2.RequestHandler):
  def post(self):
    url = models.Redirect_Url(parent=redirect_key)

    if users.get_current_user():
      url.user = users.get_current_user()

    url.to_url = self.request.get('to_url').encode('ascii','ignore')
    url.input_url = self.request.get('input_url').encode('ascii','ignore')

    if users.get_current_user() and users.is_current_user_admin():
      url.put()
      self.redirect('/')
    elif users.get_current_user():
      logging.info("Unauth'd user attempted to add entry to database")
    else:
      logging.info("Anon user attempted to add to the database")
    self.response.write("You are not authorised to perform this action")
    self.response.set_status(403)
