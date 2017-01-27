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

    url.put()
    self.redirect('/')