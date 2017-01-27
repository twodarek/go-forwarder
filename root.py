#!/usr/bin/env python
import cgi
import datetime
import logging
import models
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

class RootPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')

    self.response.out.write("""
          <form action="/new" method="post">
            <div>
                <label for="input_url">Input Url (ie: 'test' for 'http://go/test')</label>
                <textarea id="input_url" name="input_url" rows="1" cols="60"></textarea>
            </div>
            <div>
                <label for="to_url">To URL (ie: 'http://google.com')</label>
                <textarea id="to_url" name="to_url" rows="1" cols="60"></textarea>
            </div>
            <div><input type="submit" value="Add new redirect"></div>
          </form>
            <script type="text/javascript">

            function getParameterByName(name) {
               name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
               var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
               results = regex.exec(location.search);
               return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
            }

            document.getElementById('input_url').value = getParameterByName('input_url');
            </script>
        </body>
      </html>""")