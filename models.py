from google.appengine.ext import ndb
from google.appengine.api import users


class Redirect_Url(ndb.Model):

  # Username
  user = ndb.UserProperty()

  # Destination url
  to_url = ndb.TextProperty(required=True, indexed=True)

  # Url as input by the user
  input_url = ndb.TextProperty(required=True, indexed=True)

  # Computed field to compare against when making a request.  Forced to lower case
  input_url_lower = ndb.ComputedProperty(lambda self: self.input_url.lower())

