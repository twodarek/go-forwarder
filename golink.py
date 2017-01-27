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

    user = None
    logging.info(users.get_current_user())

    if users.get_current_user():
      url.user = users.get_current_user()
      user = users.get_current_user()

    url.to_url = self.request.get('to_url').encode('ascii','ignore')
    url.input_url = self.request.get('input_url').encode('ascii','ignore')

    check = users.is_current_user_admin()
    if user and users.is_current_user_admin():
      url.put()
      self.redirect('/')
    elif user:
      logging.debug(user)
      # logging.info("User %s attempted to add to the database" % (users.get_current_user())
      logging.info("Unauth'd user attempted to add entry to database")
      self.response.write("You are not authorised to perform this action")
      self.response.set_status(403)
    else:
      logging.info("Anon user attempted to add to the database")
      self.response.write("You are not authorised to perform this action")
      self.response.set_status(403)

    url.put()
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/new', GoLink)
], debug=True)
