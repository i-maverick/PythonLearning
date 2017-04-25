import time
import threading


class Writer(threading.Thread):
    buffer = ""
    lock = threading.RLock()

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        Writer.lock.acquire()
        for i in range(10):
            Writer.buffer += str(self.num)
            time.sleep(0.1)
        Writer.lock.release()


for i in range(10):
    t = Writer(i)
    t.start()

while True:
    Writer.lock.acquire()
    print(Writer.buffer)
    time.sleep(0.1)
    Writer.lock.release()
