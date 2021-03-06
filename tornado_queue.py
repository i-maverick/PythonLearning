from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=3)

@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print 'Doing work on {}'.format(item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()

@gen.coroutine
def producer():
    for item in range(5):
        yield q.put(item)
        print 'Put {}'.format(item)

@gen.coroutine
def main():
    IOLoop.current().spawn_callback(consumer)
    yield producer()
    yield q.join()
    print 'Done'

IOLoop.current().run_sync(main)