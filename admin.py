import models
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api.users import User

from permissions import Permissions as Perms


class AdminPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>HI!!</body></html>')

class CreateUser(webapp2.RequestHandler):
  def post(self):
    self.redirect('/')

app = webapp2.WSGIApplication([
  ('/admin', AdminPage),
  ('/admin/new', CreateUser)
], debug=True)
