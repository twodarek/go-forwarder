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

    # Get the destination and starting urls from the request and decode for use
    url.to_url = self.request.get('to_url').encode('ascii','ignore')
    url.input_url = self.request.get('input_url').encode('ascii','ignore')

    if user and users.is_current_user_admin():
      # Checks to see if the user is a registered admin user.  If so, allow the creation of the shortlink
      url.put()
      self.redirect('/')
    elif user:
      # This user is logged in, but not allowed to create a shortlink
      logging.debug(user)
      logging.info("Unauth'd user attempted to add entry to database")
      self.response.write("You are not authorised to perform this action")
      self.response.set_status(403)
    else:
      # Non-logged in user who attempted to create a shortlink
      logging.info("Anon user attempted to add to the database")
      self.response.write("You are not authorised to perform this action")
      self.response.set_status(403)

    url.put()
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/new', GoLink)
], debug=True)
