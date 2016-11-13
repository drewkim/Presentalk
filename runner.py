import parse
import threading
import time
from flask import Flask
import init_imgs

app = Flask(__name__)

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """
    current_parsed = ""

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        #self.images = init_imgs.get() # save API calls for now
        self.images = None
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')
            current = parse.parse(self.images)
            if current:
            	self.current_parsed = current
            time.sleep(self.interval)

    

example = ThreadingExample()

@app.route('/display/')
def display():
	current = example.current_parsed
	example.current_parsed = ""
	return current

time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')


if __name__ == '__main__':
  app.run()