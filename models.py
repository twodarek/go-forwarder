from google.appengine.ext import ndb
from google.appengine.api import users


class Redirect_Url(ndb.Model):
  user = ndb.UserProperty()
  to_url = ndb.TextProperty(required=True, indexed=True)
  input_url = ndb.TextProperty(required=True, indexed=True)
  input_url_lower = ndb.ComputedProperty(lambda self: self.input_url.lower())

