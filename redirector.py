#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

redirect_key = ndb.Key('Go Redirector', 'default_redirector')


class Redirect_Url(ndb.Model):
  user = ndb.UserProperty()
  to_url = ndb.TextProperty(required=True, indexed=True)
  input_url = ndb.TextProperty(required=True, indexed=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')

    self.response.out.write("""
          <form action="/new" method="post">
            <div>
                <label for="input_url">Input Url (ie: 'test' for 'http://go/test')</label>
                <textarea name="input_url" rows="1" cols="60"></textarea>
            </div>
            <div>
                <label for="to_url">To URL (ie: 'http://google.com'></label>
                <textarea name="to_url" rows="1" cols="60"></textarea>
            </div>
            <div><input type="submit" value="Add new redirect"></div>
          </form>
        </body>
      </html>""")


class GoLink(webapp2.RequestHandler):
  def post(self):
    url = Redirect_Url(parent=redirect_key)

    if users.get_current_user():
      url.user = users.get_current_user()
    
    url.to_url = self.request.get('to_url').encode('ascii','ignore')
    url.input_url = self.request.get('input_url').encode('ascii','ignore')

    url.put()
    self.redirect('/')

class Redirector(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    input_url = kwargs['furtherURL']
    url_parts = input_url.split('/?#')
    logging.info(url_parts)
    to_url = Redirect_Url.query(Redirect_Url.input_url == url_parts[0]).get()
    try:
        self.redirect(to_url.to_url.encode('ascii','ignore'))
    except AttributeError:
        self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/new', GoLink),
  ('/*', Redirector),
  webapp2.Route('/<furtherURL>', handler=Redirector)
], debug=True)
