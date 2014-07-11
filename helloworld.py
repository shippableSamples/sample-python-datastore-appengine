import random
import webapp2

from google.appengine.ext import ndb

class Score(ndb.Model):
  score = ndb.IntegerProperty()
  timestamp = ndb.DateTimeProperty(auto_now_add=True)

class Storage():
  def score_key(self):
    return ndb.Key('Score', 'Store')

  def populate(self):
    new_score = Score(parent=self.score_key())
    new_score.score = random.randint(1, 1234)
    new_score.put()

  def get_score(self):
    score_query = Score.query(ancestor=self.score_key()).order(-Score.timestamp)
    return score_query.get().score

class MainPage(webapp2.RequestHandler):
  def get(self):
    storage = Storage()
    storage.populate()
    score = storage.get_score()

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World %s!' % score)

application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
