import time
from celery.task import task

class NotAtomicObject(object):

  def __init__(self, size):
    self._dict = dict(zip(range(size), range(-size,size,2)))

@task
def nothing():
  return NotAtomicObject(100)
  
