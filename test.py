import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from helloworld import Storage

class HelloTestCase(unittest.TestCase):
  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()

  def tearDown(self):
    self.testbed.deactivate()

  def test(self):
    storage = Storage()
    storage.populate()
    score = storage.get_score()
    self.assertLess(score, 1234)

if __name__ == "__main__":
  unittest.main()
