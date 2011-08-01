import sys
from threading import Thread, Event
import time
import traceback
import unittest
import task

class TestResultsAreSafe(unittest.TestCase):

  def setUp(self):
    super(TestResultsAreSafe, self).setUp()
    self._startEvent = Event()
    self._threads = []
    self._exceptlist = []

  def tearDown(self):
    if not self._startEvent.isSet():
      self._startEvent.set()
      time.sleep(1)
    self._startEvent.clear()
    for thread in self._threads:
      thread.join()

  @staticmethod
  def _runATaskAndCheckItsResult(self, exeptlist):
    try:
        result = task.nothing.delay()
        self._startEvent.wait()
        while self._startEvent.isSet():
          if result.ready():
            pass
    except:
      exeptlist.append("Error: %s" % 
        ''.join(traceback.format_exception(*sys.exc_info())))

  def testRun100Threads(self):
    errors = []
    for _ in xrange(100):
      self._threads.append(
        Thread(target=self._runATaskAndCheckItsResult, 
          args=(self, errors)))
    for thread in self._threads:
      thread.start()
    time.sleep(3) #make sure all tasks completed
    self._startEvent.set()
    time.sleep(10)
    self._startEvent.clear()
    try:
      self.assertTrue(errors == [])
    except:
      for error in errors:
        print error
      raise
    print len(errors)
    for thread in self._threads:
      thread.join()

if __name__ == "__main__":
  unittest.main()
