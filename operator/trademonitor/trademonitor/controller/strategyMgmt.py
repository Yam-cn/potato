from multiprocessing import Event, Process
import time

SUBPROCESSES = []
WORKERS = []

class Worker(object):
    def __init__(self, arg="default arg"):
        super(Worker, self).__init__()
        self.arg = arg
        self.be_exit = Event()
        self.be_exit.clear()

    def stop_main_loop(self):
        print "stop_main_loop invoked"
        self.be_exit.set()

    def main_loop(self):
        print "main_loop invoked"
        print self.arg
        while not self.be_exit.is_set():
            print "do something"
            try:
                time.sleep(1)
            except Exception, e:
                print "exception occurred, ", e

        print "exit from main_loop"

def do_work(worker):
    print "do_work invoked"
    worker.main_loop()

def create_subprocess(arg):
    w = Worker(arg)
    p = Process(target=do_work, args=(w,))
    p.daemon = True
    return w, p
    
def run_strategy(strategy_id, arg):
    w, p = create_subprocess(arg)
    WORKERS.append((strategy_id, w))
    SUBPROCESSES.append((strategy_id, p))
    print WORKERS, SUBPROCESSES
    p.start()

def stop_strategy(strategy_id):
    print WORKERS
    #[w[1].stop_main_loop() for w in WORKERS if (w[0] == strategy_id)]
    for w in WORKERS:
        if (w[0] == strategy_id):
            w[1].stop_main_loop()
            WORKERS.remove(w)
    print WORKERS

if __name__ == '__main__':
    run_strategy(111, "This is a test!")
    time.sleep(2)
    run_strategy(222, "This is a test!")
    time.sleep(2)
    stop_strategy(111)
    time.sleep(2)
