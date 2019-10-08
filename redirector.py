#!/usr/bin/env python
import cgi
import datetime
import logging
import models
import webapp2

from admin import AdminPage
from golink import GoLink
from root import RootPage

from google.appengine.ext import ndb
from google.appengine.api import users


class Redirector(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    # Take the url passed from the router and parse out the interesting bits
    input_url = kwargs['furtherURL']
    url_parts = input_url.split('/?#')
    logging.info(url_parts)

    # Gets the input url from the param list, forces to lower case, and searches for it in the database
    to_url = models.Redirect_Url.query(models.Redirect_Url.input_url_lower == url_parts[0].lower()).get()

    # If the shortlink exists, redirect to it, otherwise redirect
    try:
        self.redirect(to_url.to_url.encode('ascii','ignore'))
    except AttributeError:
        self.redirect('/?input_url=' + url_parts[0])


app = webapp2.WSGIApplication([
  ('/', RootPage),
  ('/new', GoLink),
  ('/admin', AdminPage),
  ('/*', Redirector),
  webapp2.Route('/<furtherURL>', handler=Redirector)
], debug=True)
