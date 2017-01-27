#!/usr/bin/env python
import cgi
import datetime
import logging
import models
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

class AdminPage(webapp2.RequestHandler):
  def get(self):
  	self.response.out.write("Hi Admin!")

  def post(self):
  	pass