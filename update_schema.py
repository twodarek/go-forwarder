import logging
import models
from google.appengine.ext import deferred
from google.appengine.ext import ndb

BATCH_SIZE = 100  # ideal batch size may vary based on entity size.

def UpdateSchema(cursor=None, num_updated=0):
    query = models.Redirect_Url.query()
    # return, cursor, more
    a = query.fetch(BATCH_SIZE, start_cursor=cursor)

    # Yes, it's stupid, but I needed to do it this way because of the low traffic
    # I'll keep the other stuff here for larger works.
    if a:
        for p in a:
            p.input_url_lower = p.input_url.lower()
            p.put()
            num_updated += 1
        logging.debug(
            'Put %d entities to Datastore for a total of %d',
            num_updated, num_updated)
        
        #deferred.defer(
        #    UpdateSchema, cursor=p[-2], num_updated=num_updated)
    else:
        logging.debug(
            'UpdateSchema complete with %d updates!', num_updated)

